
# Python modules
from __future__ import division, print_function, absolute_import

import os
import sys
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
import vespa.analysis.util_import         as util_import
import vespa.analysis.util_file_import    as util_file_import
import vespa.analysis.figure_layouts      as figure_layouts

import vespa.common.util.misc   as util_misc
import vespa.common.util.export as util_export
import vespa.common.util.time_  as util_time


# TODO - bjs Future work and thoughts:
# ---------------------------------------------------------
# DICOM Tag for lots of text ...
#
# Need to stack Exception messages to create call stack info as it propagates up the program
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
 Command line interface to process MRS data inline with an MR scanner 
 using the Vespa-Analysis package.
  
 Note. You may have to enclose data/preset/output strings in double 
 quotation marks for them to process properly if they have  
 spaces or other special characters embedded in them.
"""


#==============================================================================
# Helper Classes and Methods

class CliError(Exception):
    """Basic exception for errors when applying preset object"""
    def __init__(self, msg=None):
        if msg is None:
            # set default error message
            msg = 'A general cli error occured.'
        e = sys.exc_info()
        msg =  'CliErrorMessage : '+msg
        msg += '\n'
        msg += 'BaseErrorMessage: '+str(e)
        super(CliError, self).__init__(msg)


class cli_output_settings:

    def __init__(self):

        module_path = os.path.abspath(__file__)
        base_path   = os.path.dirname(module_path)

        self.vespa_version = 'Vespa-CLI'

        self.save_xml = False
        self.xml_fname          = ''
        self.xml_fname_unique   = False  # append timestamp while saving

        self.save_pdf = False
        self.pdf_fname          = ''
        self.pdf_fname_unique   = False  # append timestamp while saving
        self.pdf_plotstyle      = 'lcm_multi'
        self.pdf_file_label     = 'default_pdf'
        self.pdf_inbuf          = False
        self.pdf_minppm         = 0.5
        self.pdf_maxppm         = 4.2
        self.pdf_apply_phase    = False
        self.pdf_remove_base    = False
        self.pdf_fontname       = 'Courier New'
        self.pdf_dpi            = 300
        self.pdf_pad_inches     = 0.5

        self.save_png = False
        self.png_fname          = ''
        self.png_fname_unique   = False  # append timestamp while saving
        self.png_plotstyle      = 'lcm'
        self.png_file_label     = 'default_png'
        self.png_inbuf          = False
        self.png_minppm         = 0.5
        self.png_maxppm         = 4.2
        self.png_apply_phase    = False
        self.png_remove_base    = False
        self.png_fontname       = 'Courier New'
        self.png_dpi            = 100
        self.png_pad_inches     = 0.5

        self.save_dcm           = False
        self.dcm_fname          = ''

        self.save_err           = True
        self.err_fname          = os.path.join(base_path,'default_err.png')
        self.err_fname_unique   = True
        self.err_dpi            = 100
        self.err_pad_inches     = 0.5


def is_dicom(filename):
    """
    Returns True if the file in question is a DICOM file, else False.

    Per the DICOM specs, a DICOM file starts with 128 reserved
    bytes followed by "DICM".

    ref: DICOM spec, Part 10: Media Storage and File Format for Media
         Interchange, 7.1 DICOM FILE META INFORMATION

    """
    if os.path.isfile(filename):
        f = open(filename, "rb")
        s = f.read(132)
        f.close()
        pattern = "DICM"
        binary_pattern = pattern.encode()
        return s.endswith(binary_pattern)
    else:
        return False


def get_time():

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


#==============================================================================
# CLI Interface Methods


def analysis_cli_chain(datasets, presets,
                                 basis_mmol,
                                 verbose=False,
                                 debug=False,
                                 process_id='single'):
    
    # Test keyword values -----------------------------------------------------
    


    # Sort datasets into variables --------------------------------------------
    
    data_metab,   data_water,   data_coil,    data_ecc   = datasets
    preset_metab, preset_water, preset_coil,  preset_ecc = presets

    msg = ""
    
    try:
        # --------------------------------------------------------------------------
        # Preset/Process Coil Combine Dataset

        if data_coil is not None:
            msg = process_id + " - apply preset - coil combine"
            if verbose: print(msg)
            data_coil.apply_preset(preset_coil, voxel=(0, 0, 0))  # update dataset object with preset blocks and chains

            msg = process_id + " - run chain - coil combine"
            if verbose: print(msg)
            _process_all_blocks(data_coil)

        # ----------------------------------------------------------------------
        # Apply presets to ecc, water and metab datasets

        if data_ecc is not None and preset_ecc is not None:
            msg = process_id+" - apply preset - ecc"
            if verbose: print(msg)
            data_ecc.apply_preset(preset_ecc, voxel=(0,0,0))

        if data_water is not None and preset_water is not None:
            msg = process_id+" - apply preset - water"
            if verbose: print(msg)
            data_water.apply_preset(preset_water, voxel=(0,0,0))  

        if data_metab is not None and preset_metab is not None:
            msg = process_id+" - apply preset - metab"
            if verbose: print(msg)
            data_metab.apply_preset(preset_metab, voxel=(0,0,0))  

        #----------------------------------------------------------------------
        # Attach coil combine to ecc, water and metab datasets - run chain ecc

        if data_coil is not None:
            msg = process_id+" - attach coil combine to - ecc, water and metab"
            if verbose: print(msg)
            for dset in [data_ecc, data_water, data_metab]:
                if dset is not None:
                    dset.set_associated_dataset_combine(data_coil)

        if data_ecc is not None:
            msg = process_id+" - run chain - ecc"
            if verbose: print(msg)
            _process_all_blocks(data_ecc)       # get combined FID for next steps

        #----------------------------------------------------------------------
        # Attach ecc to water and metab datasets - run chain water

        if data_ecc is not None:
            msg = process_id+" - attach ecc to - water and metab"
            if verbose: print(msg)
            for dset in [data_water, data_metab]:
                if dset is not None:
                        dset.set_associated_dataset_ecc(data_ecc)
        
        if data_water is not None:
            msg = process_id+" - run chain - water"
            if verbose: print(msg)
            _process_all_blocks(data_water)

        #----------------------------------------------------------------------
        # Attach mmol_basis and water to metab dataset - run chain metab


        for dset in [data_metab,]:
            if basis_mmol is not None:
                if dset is not None:
                    msg = process_id + " - attach mmol_basis to - metab"
                    if verbose: print(msg)
                    dset.set_associated_dataset_mmol(basis_mmol)
            msg = process_id + " - attaching water to - metab"
            if verbose: print(msg)
            dset.set_associated_dataset_quant(data_water)

        msg = process_id+" - run chain - metab"
        if verbose: print(msg)
        _process_all_blocks(data_metab)

    except Exception as e:
        msg = 'Exception (analysis_cli_chain): '+msg
        if verbose: print(msg)
        raise CliError(msg)

    return data_metab
    
    
    
def analysis_cli_output(data_metab, settings, debug=False, verbose=False, process_id='single'):

    # Test keyword values -----------------------------------------------------

    if settings is None:
        settings = cli_output_settings()


    tstamp       = util_time.now(util_time.DISPLAY_TIMESTAMP_FORMAT)
    fname_tstamp = util_time.filename_timestamp()  # yyyymmdd.hhmmss.usecs

    # determine a default output base name, just in case

    if data_metab.dataset_filename != '':
        fdefault = data_metab.dataset_filename
    elif data_metab.blocks['raw'].data_sources[0] != '':
        fdefault = data_metab.blocks['raw'].data_sources[0]
    else:
        fdefault = '.' + os.sep + 'default_out'

    #--------------------------------------------------------------------------
    # Save Dataset to XML for provenance

    if settings.save_xml:

        # Determine if an output filename exists or can be created ------------
        if settings.xml_fname == '':
            fpath, fname = os.path.split(os.path.abspath(fdefault))
            fbase, fext  = os.path.splitext(fname)
            xml_fname = fpath + os.sep + fbase + '.xml'
        else:
            xml_fname, _ = os.path.splitext(settings.xml_fname)

        # Create unique name ID for this dataset ------------------------------
        if settings.xml_fname_unique:
            xml_fname += '_'+fname_tstamp

        xml_fname += '.xml'

        data_metab.dataset_filename = xml_fname

        msg = process_id+" - Saving dataset to XML file %s. " % xml_fname
        if verbose: print(msg)

        try:
            util_export.export(xml_fname, [data_metab,], None, None, False)
        except Exception as e:
            msg = 'Exception (analysis_cli_output): '+process_id+' - Failed writing the XML file %s.' % xml_fname
            if verbose: print(msg)
            raise CliError(msg)

    #--------------------------------------------------------------------------
    # Save results to PDF

    if settings.save_pdf:

        fig_call = figure_layouts.null_call         # default

        # Determine if an output filename exists or can be created ------------
        if settings.pdf_fname == '':
            fpath, fname = os.path.split(os.path.abspath(fdefault))
            fbase, fext  = os.path.splitext(fname)
            pdf_fname = fpath + os.sep + fbase
        else:
            pdf_fname, _ = os.path.splitext(settings.pdf_fname)

        # Create unique name ID -----------------------------------------------
        if settings.pdf_fname_unique:
            pdf_fname += '_'+fname_tstamp

        if settings.pdf_plotstyle == 'lcm':
            pdf_fname  += '_lcm.pdf'
            fig_call = figure_layouts.lcm_like
        elif settings.pdf_plotstyle == 'lcm_multi':
            pdf_fname += '_lcm_multi.pdf'
            fig_call = figure_layouts.lcm_multipage_pdf

        msg = process_id+" - Saving Results to PDF %s " % pdf_fname
        if verbose: print(msg)

        try:
            figs = fig_call(data_metab,
                            viffpath=settings.pdf_file_label,
                            vespa_version=settings.vespa_version,
                            timestamp='',
                            fontname=settings.pdf_fontname,
                            minplot=settings.pdf_minppm,
                            maxplot=settings.pdf_maxppm,
                            nobase=settings.pdf_remove_base,
                            extfig=None,
                            fixphase=settings.pdf_apply_phase,
                            verbose=False,
                            debug=False,
                            quantvals=True)

            # Create the PdfPages object to which we will save the pages:
            # The with statement endsures object closed at end of block, even if Exception
            with PdfPages(pdf_fname) as pdf:
                for fig in figs:
                    pdf.savefig(fig, dpi=settings.pdf_dpi,
                                     pad_inches=settings.pdf_pad_inches,
                                     facecolor=fig.get_facecolor(),
                                     edgecolor='none')

                # We can also set the file's metadata via the PdfPages object:
                today = datetime.date.today()
                d = pdf.infodict()
                d['Title']        = u'Vespa Output - PDF'
                d['Author']       = u'Brian J. Soher'
                d['Subject']      = u'Vespa results output'
                d['Keywords']     = u'PdfPages Vespa output lcm multi-page'
                d['CreationDate'] = datetime.datetime(today.year, today.month, today.day)
                d['ModDate']      = datetime.datetime.today()

        except Exception as e:
            msg = 'Exception (analysis_cli_output): '+process_id+' - Failed to create/write PDF file %s.' % pdf_fname
            if verbose: print(msg)
            raise CliError(msg)

    # Create PNG output -------------------------------------------

    cbuf = None             # default setting
    if settings.save_png:

        # Determine if an output filename exists or can be created ------------
        if settings.png_fname == '':
            fpath, fname = os.path.split(os.path.abspath(fdefault))
            fbase, fext  = os.path.splitext(fname)
            png_fname = fpath + os.sep + fbase
        else:
            png_fname, _ = os.path.splitext(settings.png_fname)

        # Create unique name ID -----------------------------------------------
        if settings.png_fname_unique:
            png_fname += '_'+fname_tstamp

        if settings.png_plotstyle == 'lcm':
            fig_call = figure_layouts.lcm_like
        elif settings.png_plotstyle == 'lcm_multi':
            fig_call = figure_layouts.lcm_multipage_pdf
        elif settings.png_plotstyle == 'brp_generic':
            fig_call = figure_layouts.analysis_brp_generic

        msg = process_id+" - creating PNG results "
        if verbose: print(msg)

        try:
            fig = fig_call( data_metab,
                            viffpath=settings.png_file_label,
                            vespa_version=settings.vespa_version,
                            timestamp=tstamp,
                            fontname=settings.png_fontname,
                            minplot=settings.png_minppm,
                            maxplot=settings.png_maxppm,
                            nobase=settings.png_remove_base,
                            extfig=None,
                            fixphase=settings.png_apply_phase,
                            verbose=False, debug=False)

            buf1 = fig[0].canvas.tostring_rgb()

            # convert string to byte arry and (optional) write to a debug file
            cbuf = np.fromstring(buf1, dtype=np.uint8)

            msg = process_id+" - saving debug PNG file to - "+str(png_fname+'.png')
            if verbose: print(msg)
            fig[0].savefig( png_fname+'.png',
                            dpi=settings.png_dpi,
                            pad_inches=settings.png_pad_inches)

            if debug:
                msg = process_id+" - saving debug NPY file to - "+str(png_fname+'_cbuf.npy')
                if verbose: print(msg)
                cbuf.tofile(png_fname+'_cbuf.npy')

        except Exception as e:
            msg = 'Exception (analysis_cli_output): '+process_id+' - Failed to create/write file %s.' % png_fname
            if verbose: print(msg)
            raise CliError(msg)

    if verbose: print(process_id+' - finished analysis_cli_output()')

    return cbuf
            
            
               
def _process_all_blocks(dataset):
    """ for all voxels, run chain in all blocks to update """
    
    chain_outputs = {}
    
    voxel = dataset.all_voxels
    for key in dataset.blocks.keys():
        if key == 'spectral':
            key = 'spectral'
            block = dataset.blocks[key]
            tmp = block.chain.run(voxel, entry='all')
            chain_outputs[key] = tmp
            if 'fit' in dataset.blocks.keys():
                key = 'fit'
                block = dataset.blocks[key]
                block.chain.run(voxel, entry='initial_only')
                key = 'spectral'
                block = dataset.blocks[key]
                block.set_do_fit(True, voxel[0])
                tmp = block.chain.run(voxel, entry='all')
                chain_outputs[key] = tmp
        else:
            block = dataset.blocks[key]
            tmp = block.chain.run(voxel, entry='all')
            chain_outputs[key] = tmp

    return chain_outputs



def _load_preset(presetfile, verbose=False, debug=False, process_id='single'):
    """ Load Vespa-Analsys preset file """

    if not presetfile:      # this functionality required by 'analysis_kernel()'
        return None

    msg = process_id+" - load_preset - fname = %s"  % presetfile
    if verbose: print(msg)
    if debug: return None
     
    try:
        msg = ""
        try:
            importer = util_import.DatasetImporter(presetfile)
        except IOError:
            msg = process_id+" - I can't read the preset file %s." % presetfile
        except SyntaxError:
            msg = process_id+" - The preset file %s isn't valid Vespa Interchange File Format." % presetfile

        if msg:
            msg = 'Exception (_load_preset): '+msg
            if verbose: print(msg)
            raise CliError(msg)
        else:
            # Time to rock and roll!
            presets = importer.go()
            preset  = presets[0]
    except Exception as e:
        msg = 'Exception (_load_preset): '+process_id+' - Unknown exception reading Preset file %s.' % presetfile
        if verbose: print(msg)
        raise CliError(msg)

    return preset


def analysis_kernel(params, debug=False, verbose=False, process_id='single'):
    
    fdatasets, fpresets, fbasis_mmol, dataformat, settings = params

    try:
        if verbose:
            print(process_id + ' - Begin - metab filename = ' + fdatasets['metab'])

        msg = 'loading presets'
        presets = []
        for key in ['metab','water','ecc','coil']:
            fname = fpresets[key]
            if fname is not None:
                presets.append(_load_preset(fname, verbose=True, debug=debug, process_id=process_id))
            else:
                presets.append(None)

        msg = 'loading datasets'
        datasets = []
        for key in ['metab', 'water', 'ecc', 'coil']:
            fname = fdatasets[key]
            
            if fname is not None:
                dataset = util_file_import.get_datasets_cli(fname, dataformat, None)
                datasets.append(dataset[0])                
            else:
                datasets.append(None)

        msg = 'loading mmol basis'
        if fbasis_mmol is not None:
            basis_mmol, msg = util_file_import.open_viff_dataset_file([fbasis_mmol,]) 
        else:
            basis_mmol = None

        msg = 'run cli_chain'
        data_metab = analysis_cli_chain(datasets, presets, basis_mmol,
                                        debug=debug,
                                        verbose=verbose,
                                        process_id=process_id)

        msg = 'run cli_output'
        png_buf = analysis_cli_output( data_metab, settings,
                                       debug=debug,
                                       verbose=verbose,
                                       process_id=process_id)

        if verbose:
            print(process_id+' - Finish - metab filename = ' + fdatasets['metab'])
        
    except Exception as e:
        msg  = 'Exception (analysis_kernel): '+process_id+' - Error in step = '+msg
        if verbose: print(msg)
        raise CliError(msg)
            
    return png_buf
    



def do_main():
    """
    no unit test implemented yet
    
    """
    pass




if __name__ == '__main__':
    
    do_main()


