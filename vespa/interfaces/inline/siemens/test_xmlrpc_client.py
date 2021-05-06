#!/usr/bin/env python

# Python modules
import os
import base64
import xmlrpclib
import collections

# Third party modules
import numpy as np
import matplotlib.pyplot as plt

# Our modules
import vespa.common.util.misc as util_misc
import vespa.common.twix_parser as twix_parser
import vespa.common.mrs_data_raw_cmrr_slaser as mrs_data_raw_cmrr_slaser

from vespa.common.constants import DEFAULT_PROTON_CENTER_PPM, DEFAULT_XNUCLEI_CENTER_PPM

# Change to True to enable the assert() statements sprinkled through the code
ASSERTIONS_ENABLED = False



def main():

    #----------------------------------------------------------------
    # Connect to XMLRPC Server

    s = xmlrpclib.ServerProxy('http://127.0.0.1:8080')

    #----------------------------------------------------------------
    # Run Tests
    # - all worked as of 2021-05-04

    # print 'bump2 - ', s.bump2(2,3)  # Returns [3,4]
    # print 'add  - ', s.add(2,3)     # Returns 5
    # print 'div   - ', s.div(5,2)    # Returns 5//2 = 2
    # print s.system.listMethods()    # Print list of available methods
    #
    # dataf = np.arange(64)
    # dataf = dataf.tobytes()
    # dataf = xmlrpclib.Binary(dataf)         #dataf = base64.b64encode(dataf)
    # r = s.test_binary(dataf)
    #
    # #img = s.get_fake_result(1)      # 0-return fake data, 1-return all zeros
    #
    # bob = 10


    #----------------------------------------------------------------
    # Read in Twix data

    data_type = 'sead'      # 'sead' or 'seF'
    base_path = r'D:/Users/bsoher/code/repo_github/vespa_py2/vespa/interfaces/inline/siemens/datadir'

    if data_type == 'sead':
        fname = os.path.join(base_path, 'meas_MID00319_FID144443_wm_slaser028_avg32_wref1_resolv.dat')
    elif data_type == 'seF':
        fname = os.path.join(base_path, 'meas_MID00321_FID144445_wm_press030_met_avg32.dat')

    scans, evps = twix_parser.read(fname)
    d = _extract_parameters(evps)
    datain = _read_data(scans, d)
    datain = datain.astype(np.complex64)    # same as scanner (I think)

    datain = datain.tobytes()
    datain = xmlrpclib.Binary(datain)

    ncoil = d["ncoil"]
    navg  = int(len(scans) / ncoil)

    ncol        = d["dims"][0]
    acqdim0     = ncol * int(d["readout_os"])
    ncha        = d["ncoil"]
    nave        = d["navg"]
    navg        = int(len(scans) / ncoil)       # include nref+nprep
    nprep       = d["nprep"]
    nref        = d["nref"]
    os_remove   = d["remove_os"]
    nleft       = scans[0].free_parameters[0]
    nright      = 0
    os_factor   = d["readout_os"]
    dwell       = 1.0 / d["sw"]
    freq        = d["frequency"]
    delta       = 0.0
    seqte       = d["seqte"]
    nucstr      = d["nucleus"]
    seqstr      = d["sequence_type"]
    tap_point   = 1

    buf = s.vespa_process(acqdim0, ncha, nave, nprep, nref, os_remove, nleft, nright, os_factor, dwell, freq, delta, seqte, nucstr, seqstr, tap_point, datain)

    bob = 10


    nbuf = buf
    fname = os.path.join(base_path, 'vespa_inline_result_out.png')
    plt.imsave(fname, nbuf)


    bob += 1

    s.quit()

    bob += 1

#----------------------------------------------------------------------
# Utility methods

def _extract_parameters(evps):

    header, clean_header = _parse_protocol_data(evps[3][1])

    remove_oversample_flag = header.get("sSpecPara.ucRemoveOversampling", "0x0")
    remove_oversample_flag = (remove_oversample_flag.strip() == "0x1")

    d = {}
    d["header"] = clean_header
    d["sw"] = 1.0 / (float(header.get("sRXSPEC.alDwellTime[0]", 1.0)) * 1e-9)
    d["remove_os"] = remove_oversample_flag

    # Workaround for when there is not ReadoutOS found (empty ICE) in header
    # so 'remove_os' and 'readout_os' were at odds. Now default to 2 if
    # 'Remove OS' true and ReadoutOS can not be found
    def_os_factor = 2 if d["remove_os"] else 1

    d["readout_os"]     = float(_get_siemens_xprotocol(evps[0][1], "ReadoutOS", def_os_factor))
    d["sequence_type"]  = header.get("tSequenceFileName", "slaser_cmrr")
    d["frequency"]      = float(header["sTXSPEC.asNucleusInfo[0].lFrequency"]) / 1000000.0
    d["dims"]           = mrs_data_raw_cmrr_slaser.DataRawCmrrSlaser.DEFAULT_DIMS
    d["dims"][0]        = int(header["sSpecPara.lVectorSize"])
    d["dims"][1]        = 1  # concat will take care of header["lAverages"]
    d["dims"][2]        = 1
    d["dims"][3]        = 1
    d["seqte"]          = float(header["alTE[0]"]) * 1e-6
    d["nucleus"]        = header["sTXSPEC.asNucleusInfo[0].tNucleus"].replace('"', ' ').strip()

    d["midppm"] = DEFAULT_PROTON_CENTER_PPM if d["nucleus"]=='1H' else DEFAULT_XNUCLEI_CENTER_PPM

    # Parameters unique to sLASER from CMRR
    # ------------------------------------------
    d["navg"] = int(header['lAverages'])
    d["nref"] = int(header['sWiPMemBlock.alFree[43]'])
    d["ncoil"] = int(sum('lRxChannelConnected' in s for s in header.keys()))  # assumes this is unique substring

    if 'sSpecPara.lPreparingScans' in header.keys():
        d["nprep"] = int(header['sSpecPara.lPreparingScans'])
    else:
        d["nprep"] = 0

    print 'nprep/nref/navg/ncoil = '+str(d["nprep"])+'  '+str(d["nref"])+'  '+str(d["navg"])+'  '+str(d["ncoil"])

    return d


def _read_data(scans, d):

    ncoil   = d["ncoil"]
    navg    = int(len(scans) / ncoil)
    dims    = d["dims"]
    acqdim0 = dims[0] * int(d["readout_os"])

    data = np.ndarray([ncoil, navg, acqdim0], dtype=complex)

    # determine if there are any extra points at the beginning or end of FID
    start_point = scans[0].free_parameters[0]
    end_point = start_point + acqdim0

    iscan = 0
    for iavg in range(navg):
        for ichan in range(ncoil):
            chan = scans[iscan]
            data[ichan, iavg, :] = np.array(chan.data[start_point:end_point])
            iscan += 1

    return data


def _parse_protocol_data(protocol_data):
    """
    Returns a dictionary containing the name/value pairs inside the
    "ASCCONV" section of the MrProtocol or MrPhoenixProtocol elements
    of a Siemens CSA Header tag.

    """
    start = protocol_data.find("### ASCCONV BEGIN")
    end = protocol_data.find("### ASCCONV END ###")

    _my_assert(start != -1)
    _my_assert(end != -1)

    clean_start = start
    clean_end = end + len("### ASCCONV END ###")
    clean_header = protocol_data[clean_start:clean_end]

    start += len("### ASCCONV BEGIN ###")
    protocol_data = protocol_data[start:end]

    lines = protocol_data.split('\n')
    lines = lines[1:]

    # The two lines of code below turn the 'lines' list into a list of
    # (name, value) tuples in which name & value have been stripped and
    # all blank lines have been discarded.
    f = lambda pair: (pair[0].strip(), pair[1].strip())
    lines = [f(line.split('=')) for line in lines if line]

    return dict(lines), clean_header


def _my_assert(expression):
    if ASSERTIONS_ENABLED:
        assert (expression)


def _get_siemens_xprotocol(head_only, key, default):

    head = util_misc.normalize_newlines(head_only)
    head = head.split("\n")

    # find substring 'key' in list even if item in list is not iterable
    items = [el for el in head if isinstance(el, collections.Iterable) and (key in el)]

    for item in items:
        start = item.find("{")
        end = item.find("}")
        if start != -1 and end != -1:
            temp = item[start + 1:end]
            # remove duplicate white space
            temp = " ".join(temp.split())
            temp = temp.split()

            if len(temp) == 1:
                return temp[0]
            elif len(temp) == 3:
                return temp[2]
            else:
                return temp

    return default



if __name__ == '__main__':
    main()


#------------------------------------------
# Here starts another example, that matches the one in text_xmlrpc_server at the BOTTOM
#  from  https://pymotw.com/2/xmlrpclib/


# import xmlrpclib
# 
# server = xmlrpclib.ServerProxy('http://localhost:9000')
# 
# print 'Ping:', server.ping()
# 
# 
# server = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)
# print 'Allowed:', server.show_type(None)
# 
# server = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=False)
# print 'Not allowed:', server.show_type(None)
# 
# 
# 
# for t, v in [ ('boolean', True), 
#               ('integer', 1),
#               ('floating-point number', 2.5),
#               ('string', 'some text'), 
#               ('datetime', datetime.datetime.now()),
#               ('array', ['a', 'list']),
#               ('array', ('a', 'tuple')),
#               ('structure', {'a':'dictionary'}),
#             ]:
#     print '%-22s:' % t, server.show_type(v)
#     
#     
# 
# 
# s = 'This is a string with control characters' + '\0'
# print 'Local string:', s
# 
# data = xmlrpclib.Binary(s)
# print 'As binary:', server.send_back_binary(data)
# 
# print 'As string:', server.show_type(s)
# 
# 
# 
# try:
#     server.raises_exception('A message')
# except Exception, err:
#     print 'Fault code:', err.faultCode
#     print 'Message   :', err.faultString