# Python modules
from __future__ import division

# Spin echo profile for 180 SE pulse
# Called by mplcalcc

# Note that splotn etc removed for now


# :FIXME: Sections commented out with 
# triple quotes (''')
# will be converted to python, and what is
# useful will be moved into slr_pulse

# Declare globals
'''global mpgbb mpgaa mpgnofp mpgdtmu mpgang'''


'''
# function [ax,profile] = mplsepro(expan,pcde)
def mplsepro(expan, pcde):    
    pass
    
    # Declare local variables 
    h = mpgbb 
    a = mpgaa 
    na = mpgnofp 
    ang = mpgang
    
    nq = 1000/(2*mpgdtmu)
    
    # Initialize plot code constants and decode pcde
    
    mag = 0 
    magex = 0 
    magre = 0 
    slog = 0
    
    # Trap for pcde = 8 
    if pcde == 8:
        pcde = 0
        
    if pcde > 8:
        slog = 1 
        pcde = pcde - 8 
        
    if pcde > 3:
        magre = 1 
        pcde = pcde - 4 
        
    if pcde > 1:
        magex = 1 
        pcde = pcde - 2
        
    if pcde == 1: 
        mag = 1
    
    # Set mmgfincr 
    figure 
    mmgfincr = gcf 
    close(gcf)
    
    # Rearrange h for plotting
    
    h = h'    # Convert to row vector
    l = length(h)
    hn = [h(l/2 +1:l) h(1:l/2)]
    
    # mag 
    if mag == 1:
    
        wn = -1:2/l:(l-1)/l
        ax = wn*nq 
        profil = (hn.*hn)
        
        mmgfincr = mmgfincr + 1
        mplnfxyoff = mmgfxyoff*mmgfincr
        mplnfxypos = mmgfxypos + mplnfxyoff
        
        # New figure window
        figure('Position',mplnfxypos)   
            
        plot(ax, abs(profil))
        title('SPIN-ECHO SLICE PROFILE')
        xlabel('Frequency (KHz)') 
        ylabel('Mxy Abs Amplitude')
        
        # Write id 
        mmgplotns = num2str(mmgplotn)
        hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
        'Color','yellow','Rotation', 90)
    
    
        if slog == 1: 
            mmgfincr = mmgfincr + 1
            mplnfxyoff = mmgfxyoff*mmgfincr
            mplnfxypos = mmgfxypos + mplnfxyoff
            figure('Position',mplnfxypos)    # New figure window
            
            semilogy(ax,abs(abs(cos(ang))-abs(profil)) )
            title('LOG IN-SLICE RIPPLE')
            xlabel('Frequency (KHz)');ylabel('Log Delta Mxy Abs Amplitude');
            
            # Write id 
            mmgplotns = num2str(mmgplotn)
            hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
            'Color','yellow','Rotation', 90)
      
        
            mmgfincr = mmgfincr + 1
            mplnfxyoff = mmgfxyoff*mmgfincr
            mplnfxypos = mmgfxypos + mplnfxyoff
            figure('Position',mplnfxypos)    # New figure window
        
            semilogy(ax,abs(profil))
            title('LOG OUT-OF-SLICE RIPPLE')
            xlabel('Frequency (KHz)') 
            ylabel('Log Mxy Abs Amplitude')
                
            # Write id 
            mmgplotns = num2str(mmgplotn)
            hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
            'Color','yellow','Rotation', 90)
    
    # magex
    if magex == 1:
    
        le = ceil(l/expan) 
        le = 2*ceil(le/2) # Ensure le even
        hnp = hn((l-le)/2+1:(l+le)/2)
        wn = -le/l:2/l:(le-1)/l 
        ax = wn*nq
        
        profil = hnp.*hnp
        
        mmgfincr = mmgfincr + 1
        mplnfxyoff = mmgfxyoff*mmgfincr
        mplnfxypos = mmgfxypos + mplnfxyoff
        figure('Position',mplnfxypos)    # New figure window
        
        plot(ax, abs(profil),'r')
        title('SPIN-ECHO SLICE PROFILE')
        xlabel('Frequency (KHz)') 
        ylabel('Mxy Abs Amplitude')
        
        # Write id 
        mmgplotns = num2str(mmgplotn)
        hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
        'Color','yellow','Rotation', 90)
    
    
        if slog == 1: 
    
            mmgfincr = mmgfincr + 1
            mplnfxyoff = mmgfxyoff*mmgfincr
            mplnfxypos = mmgfxypos + mplnfxyoff
            figure('Position',mplnfxypos)    # New figure window
            
            semilogy(ax,abs(abs(cos(ang))-abs(profil)),'r')
            title('LOG IN-SLICE RIPPLE')
            xlabel('Frequency (KHz)');ylabel('Log Delta Mxy Abs Amplitude');
            
            # Write id 
            mmgplotns = num2str(mmgplotn)
            hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
            'Color','yellow','Rotation', 90)
        
        
            mmgfincr = mmgfincr + 1
            mplnfxyoff = mmgfxyoff*mmgfincr
            mplnfxypos = mmgfxypos + mplnfxyoff
            figure('Position',mplnfxypos)    # New figure window
            
            semilogy(ax,abs(profil),'r')
            title('LOG OUT-OF-SLICE RIPPLE')
            xlabel('Frequency (KHz)') 
            ylabel('Log Mxy Abs Amplitude')
            
            # Write id 
            mmgplotns = num2str(mmgplotn)
            hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
            'Color','yellow','Rotation', 90)
    
    
    # magre 
     if magre == 1:
        
        le = ceil(l/expan) 
        le = 2*ceil(le/2) # Ensure le even
        hnp = hn((l-le)/2+1:(l+le)/2)
        wn = -le/l:2/l:(le-1)/l 
        ax = wn*nq
        wq = pi*wn 
        rot = exp(-i*(wq*(na-1)))
        profil = (hnp.*hnp)
        profil = profil.*rot
    
        mmgfincr = mmgfincr + 1
        mplnfxyoff = mmgfxyoff*mmgfincr
        mplnfxypos = mmgfxypos + mplnfxyoff
        figure('Position',mplnfxypos)    # New figure window
        
        plot(ax, real(profil),ax,imag(profil),'g-.')
        title('SPIN-ECHO SLICE PROFILE')
        xlabel('Frequency (KHz)') 
        ylabel('Mx and My Amplitude')
    
        # Write id 
        mmgplotns = num2str(mmgplotn)
        hid = text(1.04, 1.0, mmgplotns,'Units','normalized', ...
        'Color','yellow','Rotation', 90)

'''

