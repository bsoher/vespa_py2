
# Python modules
from __future__ import division, print_function, absolute_import

import argparse
import os
import sys
import platform 
import imp
import xml.etree.cElementTree as ElementTree
import collections
import multiprocessing
import datetime

# 3rd party modules
import numpy as np
try:
    import dicom
except:
    import pydicom as dicom

from matplotlib.backends.backend_pdf import PdfPages

# Third party modules


# Our modules
import vespa.analysis.inline.vespa_inline_engine as vie
#from vespa_inline_engine import is_dicom, cli_output_settings, CliError, analysis_kernel
import vespa.analysis.util_import as util_import
import vespa.analysis.util_file_import as util_file_import
import vespa.analysis.figure_layouts as figure_layouts
import vespa.analysis.fileio.util_philips as util_philips

import vespa.common.util.misc as util_misc
import vespa.common.util.export as util_export
import vespa.common.util.time_ as util_time




# TODO - bjs Future work and thoughts:
# ---------------------------------------------------------
# DICOM Tag for lots of text ...
#
# Can use any input/output directories, maybe an ini file for users to modify?
#  or std locs if ini not available
#
# can ditch STD mix=1 data, but should modify parser in future to keep in keyword optional
#
# Show work flow for


# Change to True to enable the assert() statements sprinkled through the code
ASSERTIONS_ENABLED = False




DESC =  \
"""
 Command line interface to process Philip MRS data inline with
 the MR scanner using the Vespa-Analysis package.
  
 Note. You may have to enclose data/preset/output strings in double 
 quotation marks for them to process properly if they have  
 spaces or other special characters embedded in them.
"""


#==============================================================================
# Helper Classes and Methods



def do_main():
    """
    There are 5 processing steps:
    1. read all files from a known 'datadir', these are in DICOM MRS format
    2. decide which file is water and which is metabolite
    3. run both files through the Vespa-Analysis inline method
    4. output array gets put into a pydicom secondary capture RGB DICOM
    5. optional, save provedance XML file for debugging.
    
    """

    try:
        debug       = False
        verbose     = True
        dataformat  = 'import_philips_dicom'

        module_path = os.path.abspath(__file__)
        base_path   = os.path.dirname(module_path)
        data_dir    = os.path.join(base_path, 'datadir')
        preset_dir  = os.path.join(base_path, 'presets')
        output_dir  = os.path.join(base_path, 'output')
        debug_dir   = os.path.join(base_path, 'debug')

        settings = vie.cli_output_settings()

        settings.vespa_version      = '0.10.0-CLI'

        settings.save_xml           = True
        settings.save_pdf           = True
        settings.save_png           = True
        settings.save_dcm           = False
        settings.save_err           = True

        settings.xml_fname_unique   = True
        settings.pdf_fname_unique   = True
        settings.png_fname_unique   = True
        settings.dcm_fname_unique   = True
        settings.err_fname_unique   = True

        settings.xml_fname = os.path.join(debug_dir, "output_xml_last_run.xml")
        settings.pdf_fname = os.path.join(debug_dir, "debug_pdf_philips.pdf")
        settings.png_fname = os.path.join(output_dir,"debug_png_philips.png")
        settings.dcm_fname = os.path.join(output_dir,"output_dicom_last_run.dcm")
        settings.err_fname = os.path.join(debug_dir, "err_file_last_run.xml")

        settings.pdf_savetype       = 'lcm_multi'
        settings.pdf_file_label     = 'Analysis- Philips PRIDE Inline'
        settings.pdf_minppm         = 0.5
        settings.pdf_maxppm         = 4.2
        settings.pdf_apply_phase    = False
        settings.pdf_remove_base    = False
        settings.pdf_fontname       = 'Courier New'
        settings.pdf_dpi            = 300
        settings.pdf_pad_inches     = 0.5

        settings.png_savetype       = 'lcm'
        settings.png_file_label     = 'Analysis- Philips PRIDE Inline'
        settings.png_minppm         = 0.5
        settings.png_maxppm         = 4.2
        settings.png_apply_phase    = False
        settings.png_remove_base    = False
        settings.png_fontname       = 'Courier New'
        settings.png_dpi            = 300
        settings.png_pad_inches     = 0.5

        settings.err_dpi            = 300
        settings.err_pad_inches     = 0.5


        # ---------------------------------------------------------------
        # 1. Get filenames from known DATADIR directory

        dicom_mrs_files = []
        other_files     = []
        for dirpath, dirnames, filenames in os.walk(data_dir):
            for filename in filenames:
                ftest = os.path.join(dirpath, filename)
                if vie.is_dicom(ftest):
                    dataset = dicom.read_file(ftest, defer_size=1024)
                    if util_philips.is_mrs_dicom(dataset):
                        dicom_mrs_files.append(ftest)
                        if verbose: print('Found DICOM MRS file - '+ftest)
                else:
                    other_files.append(ftest)




        if (len(dicom_mrs_files) < 1):
            msg  = 'Exception (do_main): No MRS DICOM datasets found in - '+data_dir
            if verbose: print(msg)
            raise vie.CliError(msg)

        # ----------------------------------------------------------
        # 2. decide which file is metab and which is water

        dicom_water = dicom_mrs_files[0]
        dicom_metab = dicom_mrs_files[1]

        # ----------------------------------------------------------
        # 3. load filenames into parameter lists

        fdatasets = {'metab':None, 'water':None, 'ecc':None, 'coil':None}
        fdatasets['metab'] = dicom_metab       # metab
        fdatasets['water'] = dicom_water       # metab

        fpresets = {'metab':None, 'water':None, 'ecc':None, 'coil':None}
        fpresets['metab'] = os.path.join(preset_dir,'preset_philips_dicom_press28_metab.xml')       # metab
        fpresets['water'] = os.path.join(preset_dir,'preset_philips_dicom_press28_water.xml')       # metab

        fbasis_mmol = None       # mmol   fbase+'\\basis_mmol_dataset_seadMM2014_truncat2048pts_normScale100dc015.xml'

        # ----------------------------------------------------------
        # 4. Basic file checking for existence

        msg = ''
        for key in fdatasets.keys():
            item = fdatasets[key]
            if item is not None:
                if not os.path.isfile(item):
                    msg += """\nFILE does not exist "%s".""" % item
        for key in fpresets.keys():
            item = fpresets[key]
            if item is not None:
                if not os.path.isfile(item):
                    msg += """\nFILE does not exist "%s".""" % item
        item = fbasis_mmol
        if item is not None:
            if not os.path.isfile(item):
                msg += """\nFILE does not exist "%s".""" % item
        if msg:
            msg  = 'Exception (do_main): '+msg
            if verbose: print(msg)
            raise vie.CliError(msg)

        # ----------------------------------------------------------
        # 5. Run the processing

        params = [fdatasets, fpresets, fbasis_mmol, dataformat, settings]

        dcm_buf = vie.analysis_kernel( params, debug=debug, verbose=verbose )

    except vie.CliError as e:

        # TODO - add list of filenames and presets being used to text mesage

        fig = figure_layouts.png_error(e, fontname='Courier New' )
        buf1 = fig[0].canvas.tostring_rgb()
        dcm_buf = np.fromstring(buf1, dtype=np.uint8)

        if settings.save_err:
            fname = settings.err_fname
            if settings.err_fname_unique:
                fname += util_time.filename_timestamp()  # yyyymmdd.hhmmss.usecs

            fig[0].savefig(fname + '.png',
                           dpi=settings.err_dpi,
                           pad_inches=settings.err_pad_inches)


    except Exception as e:

        fig = figure_layouts.png_error(e, fontname='Courier New' )
        buf1 = fig[0].canvas.tostring_rgb()
        dcm_buf = np.fromstring(buf1, dtype=np.uint8)

        if settings.save_err:
            fname = settings.err_fname
            if settings.err_fname_unique:
                fname += util_time.filename_timestamp()  # yyyymmdd.hhmmss.usecs

            fig[0].savefig(fname + '.png',
                           dpi=settings.err_dpi,
                           pad_inches=settings.err_pad_inches)

        # Exception handling example from: https://stackoverflow.com/questions/4690600/python-exception-message-capturing
        #
        # import sys
        # import traceback
        #
        # try:
        #     ans = 1 / 0
        # except BaseException as ex:
        #     # Get current system exception
        #     ex_type, ex_value, ex_traceback = sys.exc_info()
        #
        #     # Extract unformatter stack traces as tuples
        #     trace_back = traceback.extract_tb(ex_traceback)
        #
        #     # Format stacktrace
        #     stack_trace = list()
        #
        #     for trace in trace_back:
        #         stack_trace.append(
        #             "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        #
        #     print("Exception type : %s " % ex_type.__name__)
        #     print("Exception message : %s" % ex_value)
        #     print("Stack trace : %s" % stack_trace)

    # ----------------------------------------------------------
    # 5.  dump dcm_buf to a DICOM RGB file ... somehow.




    print('fname_dicom = ' + settings.dcm_fname)



    bob = 10
    bob += 1




if __name__ == '__main__':
    
    do_main()


