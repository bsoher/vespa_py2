# Python imports
from __future__ import division
import xml.etree.cElementTree as ElementTree

# 3rd party imports
import numpy as np

# Vespa imports
# These imports take advantage of the fact that Python adds analysis/src to
# sys.path when analysis/src/main.py is run.
import functor 
import vespa.analysis.constants as constants
import vespa.common.util.xml_ as util_xml
import vespa.common.util.misc as util_misc
import vespa.common.util.math_ as util_math

from vespa.common.constants import Deflate

ECC_MENU_ITEMS = ['None','Klose','Quality','Quecc','Simple','Traf']

#----------------------------------------------------------
# Eddy Current Correction Algorithms

def ecc_klose(chain, ecc_raw, ecc_dataset):
    if ecc_dataset: 
        voxel = chain.voxel
        
        ecc    = ecc_raw[voxel[2],voxel[1],voxel[0],:]
        
        phecc  = np.angle(ecc)
        phtime = np.angle(chain.data)
        
        chain.data  = abs(chain.data) * util_math.safe_exp(1j*(phtime-phecc))


def ecc_quality(chain, ecc_raw, ecc_dataset):
    
    if ecc_dataset: 
        voxel = chain.voxel
        
        ecc = ecc_raw[voxel[2],voxel[1],voxel[0],:]
        
        thresh = 0.01
        indx = (abs(ecc) < thresh).nonzero()
        if len(indx[0]) > 0:
            phase = np.angle(ecc[indx[0]])
            replace = np.complex64(thresh * util_math.safe_exp(1j * phase))
            ecc[indx[0]] = replace

        chain.data  = chain.data / ecc  

     
def ecc_quecc(chain, ecc_raw, ecc_dataset):
    """
    Based on Bartha, et.al. MRM Vol 44, p.641-645, 2000
    
    "There are two important issues that must be considered when implementing 
    QUECC: determining the optimal crossover point (time) to end the QUALITY 
    deconvolution and begin the ECC, and ensuring there is no discontinuity 
    at this crossover point.
    
    Phase continuity is automatically maintained at the QUECC crossover point
    because both QUALITY deconvolution and ECC techniques subtract the phase
    of the reference from the phase of the data. In contrast, amplitude
    continuity must be actively maintained because the division of the initial
    time domain data by the reference signal (during QUALITY deconvolution)
    reduces the damping of the data by the damping of the reference (3).
    Therefore, exponential filtering by an amount equal to the damping of the
    reference signal must be applied to the QUALITY corrected data to restore
    the original spectral linewidth (damping). Filtering with the incorrect
    exponential damping constant will produce an amplitude discontinuity at
    the QUECC crossover point.
    
    Unfortunately, eddy current distortions in the unprocessed reference
    spectrum may preclude accurate measurement of the exponential damping of
    the reference signal manually or by fitting the nonlineshape corrected
    data. In this case, the magnitude of the exponential filter constant can
    be estimated by QUALITY deconvolving the initial portion of the reference
    signal (using either a second reference signal, or itself) and then
    evaluating the exponential damping constant (LB) required to equalize the
    magnitude of the last point that was QUALITY deconvolved with the
    magnitude of the first ECC point using Eq. [1]. In this study, the correct
    exponential damping constant was estimated using Eq. [1] to solve for LB;
    the point at 100 msec of the reference signal was the last point that was
    QUALITY deconvolved, and the point at 100.5 msec was the first ECC point.
    The estimation of LB using this approach was made using the same water
    unsuppressed acquisition as the "data" and the "reference"
    self-correction.
    
    FID(ta) x exp(-pi x LB x abs(Pz x dw + dt)) = FID(ta+1)
    
    FID(tx) = value of last Qualit/ECC corrected point
    LB = exponential line broadening term
    dw = dwell time
    dt = delay time
    Pq = number of points where Quality has been applied"
    
    """    
    if ecc_dataset: 
        voxel = chain.voxel
        
        ecc = ecc_raw[voxel[2],voxel[1],voxel[0],:]

        dwell = 1.0/ecc_dataset.sw
        dim0  = ecc_dataset.raw_dims[0]
        xx    = np.arange(dim0) * 1.0 * dwell
        
        # find first point where we hit the threshold
        indx  = (xx >= 0.100).nonzero()
        indx  = indx[0][0]
        if indx >= len(ecc):
            indx = len(ecc)-1

        # calc a quality

        #lb = -np.log(abs(ecc[indx]))/(np.pi * dwell * (indx-1))
        lb = -np.log(ecc[indx+1]/(ecc[indx])) / (np.pi * abs(indx * dwell))
        refapod = util_math.safe_exp(-(lb * np.pi * xx))
        qual = refapod * chain.data / ecc

        # calc an ecc

        phd  = np.angle(chain.data)
        phe  = np.angle(ecc)
        eabs = abs(ecc)
        kecc = abs(chain.data) * util_math.safe_exp(complex(0,1)*(phd-phe))

        # combine the two

        chain.data[0:indx]  = qual[0:indx]
        chain.data[indx+1:] = kecc[indx+1:]


def ecc_simple(chain, ecc_raw, ecc_dataset):
    
    if ecc_dataset: 
        voxel = chain.voxel

        ecc = ecc_raw[voxel[2],voxel[1],voxel[0],:]
        
        thresh = 0.01
        index = ((abs(ecc) < thresh).nonzero())[0]
        if len(index) > 0:
            phase = np.angle(ecc[index])
            tom = (thresh * (ecc[index]/abs(ecc[index])) * util_math.safe_exp(1j * phase)).astype('complex64')
            ecc[index] = tom
        
        chain.data  = chain.data / ecc    


def ecc_traf(chain, ecc_raw, ecc_dataset):
    
    if ecc_dataset: 

        voxel = chain.voxel

        # water reference FID
        ecc = ecc_raw[voxel[2],voxel[1],voxel[0],:]

        # metabolite FID
        met = chain.data

        # sweep width
        sw = chain.sw

        # Call _refdeca_gm wih water reference FID and sw
        # to get amplitude and phase corrections and estimated T2
        [ampcor,phasecor,t2e] = _refdeca_gm(ecc,sw)

        # Call _refdecb_gm with metabolite FID and outputs
        # from _refdeca_gm to obtained final corrected 
        # metabolite FID - modifies metaboilte FID in place
        metf = _refdecb_gm(met,ampcor,phasecor,t2e,sw)

        chain.data = metf


##### Internal helper functions ##################################


def _savitzky_golay( y, window_size, order, deriv=0):
    """
    Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
    The Savitzky-Golay filter removes high frequency noise from data.
    It has the advantage of preserving the original shape and
    features of the signal better than other types of filtering
    approaches, such as moving averages techhniques.
    Parameters

    Obtained from: http://www.scipy.org/Cookbook/SavitzkyGolay
    ----------
    y : array_like, shape (N,)
        the values of the time history of the signal.
    window_size : int
        the length of the window. Must be an odd integer number.
    order : int
        the order of the polynomial used in the filtering.
        Must be less then `window_size` - 1.
    deriv: int
        the order of the derivative to compute (default = 0 means only smoothing)
    Returns
    -------
    ys : ndarray, shape (N)
        the smoothed signal (or it's n-th derivative).
    Notes
    -----
    The Savitzky-Golay is a type of low-pass filter, particularly
    suited for smoothing noisy data. The main idea behind this
    approach is to make for each point a least-square fit with a
    polynomial of high order over a odd-sized window centered at
    the point.
    Examples
    --------
    t = np.linspace(-4, 4, 500)
    y = util_math.safe_exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
    ysg = savitzky_golay(y, window_size=31, order=4)
    import matplotlib.pyplot as plt
    plt.plot(t, y, label='Noisy signal')
    plt.plot(t, util_math.safe_exp(-t**2), 'k', lw=1.5, label='Original signal')
    plt.plot(t, ysg, 'r', label='Filtered signal')
    plt.legend()
    plt.show()
    References
    ----------
    .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
       Data by Simplified Least Squares Procedures. Analytical
       Chemistry, 1964, 36 (8), pp 1627-1639.
    .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
       W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
       Cambridge University Press ISBN-13: 9780521880688
    """
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv]
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m, y, mode='valid')


def _traf_gm( siglen, t2e, sw):
    """
    _traf_gm(siglen,t2e,sw)
    
    This function returns the standard complex TRAF filter for a
    signal length and estimated T2 (T2*) (in points) input.
    
    Input:
       siglen - signal length
       t2e - T2 (T2*) estimate (in points, i.e. relative to siglen)
    Output:
       complex TRAF filter
    
    """
    eps   = np.sqrt(np.finfo(np.float).eps)
    dwell = 1.0/float(sw)
    tim = np.arange(siglen)*dwell
    traff = np.array(np.zeros(siglen),np.complex)
    
    mE = np.zeros(siglen)
    mF = np.zeros(siglen)
    
    for i,t in enumerate(tim):
        if abs(t/t2e) < 25:
            mE[i] = util_math.safe_exp(-t/t2e)
        else:
            mE[i] = eps

    for i,t in enumerate(tim):
        if abs((tim[-1] - t)/t2e) < 25:
            mF[i] = util_math.safe_exp(-(tim[-1] - t)/t2e)
        else:
            mF[i] = 0.0
    
    mEE = mE * mE
    mFF = mF * mF
    mEF = mE * mF
    denom = mEE + mFF
    traff.real = (mEE + mEF)/denom
    traff.imag = (mEE - mEF)/denom
    
    return traff


def _refdeca_gm( dcy,sw):

    """
    _refdeca_gm(h2o_ref,sw)
    Provides amp and phase corrections from water only signal
    ASSUMES APODIZATION USED FIRST (data first point halved) *******
    Checks for excessive corrections 
    Assumes files already added (or a single file)containing only water
    Data is dcy; sw known in Hz
    Set any parameters (lwfact for narrower metab lines)
    
    Input:
       h2o_ref - a water reference FID
       sw - sweep width in Hz
    Output:
       [AmpCor,PhaseCor,T2E]
       Ampcor - amplitude correction to multiply metabolite FID by
       Phasecor - phase correction to use on metabolite FID (length
                  of FID)
       T2E - T@ estimated from water reference FID
    """
    lwfact   = 1.2
    aCorrMax = 2.0
    
    # Time points
    t = (1./sw) * np.arange(len(dcy))
    
    # Work with absolute mode to obtain T2 estimate
    # Fits to beginning and end of FID (absolute mode)
    # Restore first data point for data
    data = np.abs(dcy)
    data[0] = 2.0*data[0]
    
    # Filter FID to minimize noise
    data = _savitzky_golay(_savitzky_golay(data, 15, 3), 13, 3)
    
    # Set regions to fit (Skip first 10 pts)
    mMax1 = data[10]
    mMin1 = 2.0*mMax1/3.0 + mMax1/10.0
    mMax2 = mMax1/3.0
    mMin2 = mMax1/6.0
    
    # Find value for first T2 (=p(1))
    index_mMin1 = np.nonzero(data > mMin1)
    mExp1    = data[index_mMin1[0][9:]]
    timeFit1 =    t[index_mMin1[0][9:]]
    
    y = np.log(mExp1)
    x = timeFit1
    p = np.polyfit(x, y, 1.)
    
    # Find value for first T2 (=x(2))
    index_mMin2a = np.nonzero(data > mMin2)
    index_mMin2b = np.nonzero(data < mMax2)
    range_index = np.array([n for n in np.arange(len(data)) if ((n in index_mMin2a[0]) and (n in index_mMin2a[0]))])
    mExp2 = data[range_index]
    
    timeFit2 = t[range_index]
    if len(mExp2) > 40:
        mExp2 = mExp2[0:40]
        timeFit2 = timeFit2[0:40]

    # Find value for second T2 (=q(1))
    y = np.log(mExp2)
    x = timeFit2
    q = np.polyfit(x, y, 1.)

    mT21 = -1.0/p[0]
    mT22 = -1.0/q[0]
    mk = mT21/mT22
    mexp = 1.0 - mk
    if mT21 > mT22:
        mT2used = lwfact * mT21
    else:
        mT2used = lwfact * mT22 * mk**mexp
        
    #*********************************
    # Divide ideal into actual to obtain amplitude correction (mConAmpCor)
    # Phase correction is just negative of dcy phase (mSPhase)
    
    mSideal = util_math.safe_exp(-t/mT2used)
    aMs = np.max(data)
    mConAmpCor = aMs*mSideal/data

    iterr = 0
    if np.max(mConAmpCor) > aCorrMax:
        maxCorr = np.max(mConAmpCor)
        while maxCorr > aCorrMax:
            # Add small amount of 2 Hz line to data (do this at most twice)
            if iterr < 2:
                data = data + 0.01*aMs*util_math.safe_exp(-t*2*np.pi) ;
            # Make T2used shorter if AmpCor exceeds maximum (aCorrMax)  
            mT2used = mT2used - 0.001
            mSideal= util_math.safe_exp(-t/mT2used) ;
            mConAmpCor = aMs*mSideal/data
            maxCorr = np.max(mConAmpCor)
            iterr += 1
    
    mSPhase = np.unwrap((-np.angle(dcy)))
    
    # Filter amp and phase, and limit amp
    mConAmpCor = _savitzky_golay(_savitzky_golay(mConAmpCor, 11, 5), 9, 4)
    mSPhase    = _savitzky_golay(mSPhase, 9, 3)
    
    npts1 = len(t)
    npts2 = (1.4/npts1)*np.arange(npts1)
    mExpMul    = util_math.safe_exp((-npts2**12.0))
    mConAmpCor = mConAmpCor*mExpMul

    return [mConAmpCor, mSPhase, mT2used]


def _refdecb_gm( dcy, mConAmpCor, mSPhase, mT2used, sw):
    """
    _refdecb_gm(metab_fid,Ampcor,Phasecor,T2E)

    Uses amp and phase corrections from water only signal
    ti deconvolve a metabolite FID - aprroximates Lorentzian line
    shapes for the metabolite lines. It further applies a TRAF filter
    to improve the lineshape.
    
    Input:
       metab_fid - a metabolite FID
       Ampcor - amplitude correction to multiply metabolite FID by
       Phasecor - phase correction to use on metabolite FID (length
                  of FID)
       T2E - T@ estimated from water reference FID
    Output:
       corrected meatbolite FID
       
    """
    t2e = mT2used

    # FIRST APPLY AMP AND PHASE CORRECTIONS ************
    # Work with absolute mode to obtain T2 estimate
    # Fits to beginning and end of FID (absolute mode)
    data = np.abs(dcy)
    data[0] = 2.0*data[0]
    
    # Amp correction
    data = data*mConAmpCor
    
    # Phase correction
    phasea = np.angle(dcy)+mSPhase
    
    # Corrected data
    dcy = data*util_math.safe_exp(np.complex(1j)*phasea)
    
    #********************************************
    # NOW APPLY TRAF FILTER FROM ROUTINE TRAF_GM
    siglen = len(dcy)
    traffilter = _traf_gm(siglen, t2e, sw)
    
    realdcy = dcy*traffilter.real + (dcy*traffilter.real)[::-1]
    imagdcy = dcy*traffilter.imag - (dcy*traffilter.imag)[::-1]
    dcy = 0.5 * (realdcy + imagdcy)
    
    # Halve first pt prior to FT
    dcy[0] = dcy[0]/2.0
    
    return dcy         


def do_ecc_processing(chain):
    
    ecc_method  = chain._block.set.ecc_method
    ecc_dataset = chain._block.set.ecc_dataset
    ecc_raw     = chain._block.set.ecc_raw
    
    if ecc_method == 'Klose':
        ecc_klose(chain, ecc_raw, ecc_dataset)
        
    elif ecc_method == 'Quality':
        ecc_quality(chain, ecc_raw, ecc_dataset)
        
    elif ecc_method == 'Quecc':
        ecc_quecc(chain, ecc_raw, ecc_dataset)
        
    elif ecc_method == 'Simple':
        ecc_simple(chain, ecc_raw, ecc_dataset)
        
    elif ecc_method == 'Traf':
        ecc_traf(chain, ecc_raw, ecc_dataset)
        
        
    
    
    
    
