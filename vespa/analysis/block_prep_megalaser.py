# Python modules
from __future__ import division

# 3rd party modules
import numpy as np
import xml.etree.cElementTree as ElementTree

# Our modules
import vespa.analysis.block_prep_identity as block_prep_identity
import vespa.analysis.chain_prep_megalaser as chain_prep_megalaser
import vespa.analysis.block as block

import vespa.common.util.xml_ as util_xml
import vespa.common.util.misc as util_misc
import vespa.common.constants as common_constants
import vespa.common.mrs_data_raw as mrs_data_raw


from vespa.common.constants import Deflate



class _Settings(object):
    # The XML_VERSION enables us to change the XML output format in the future 
    XML_VERSION = "1.0.0"

    
    def __init__(self, attributes=None):
        """
        Currently there are no input parameters set in this object. This may
        change in the future, or this object may serve as a base class for
        other "raw" types of data objects that need to do a bit of massaging
        of the data as it comes in (e.g. align and sum individual FIDs for 
        an SVS data set).
        
        """
        self.fid_left_shift         = 0
        self.gaussian_apodization   = 2.0
        self.global_phase1          = 0.0
        
        self.apply_peak_shift       = True
        self.reference_peak_center  = 2.01
        self.peak_search_width      = 0.2
        self.fid_left_shift_b0      = 56
        
        self.apply_phase0           = True
        self.phase0_range_start     = 2.2
        self.phase0_range_end       = 1.8
        self.fid_left_shift_phase0  = 56
        self.ref_spectrum_source    = 'singlet_centered_in_range'
        self.ref_peak_line_width    = 18
        self.constant_phase0_offset = 70     # degrees
        
        if attributes is not None:
            self.inflate(attributes)


    def __str__(self):
        return self.__unicode__().encode("utf-8")


    def __unicode__(self):
        lines = [ ]
        lines.append("--- Block Preprocess Megalaser Settings ---")
        lines.append("fid_left_shift            : " + unicode(self.fid_left_shift))
        lines.append("gaussian_apodization      : " + unicode(self.gaussian_apodization))
        lines.append("apply_peak_shift          : " + unicode(self.apply_peak_shift))
        lines.append("reference_peak_center     : " + unicode(self.reference_peak_center))
        lines.append("peak_search_width         : " + unicode(self.peak_search_width))
        lines.append("fid_left_shift_b0         : " + unicode(self.fid_left_shift_b0))
        lines.append("apply_phase0              : " + unicode(self.apply_phase0))
        lines.append("phase0_range_start        : " + unicode(self.phase0_range_start))
        lines.append("phase0_range_end          : " + unicode(self.phase0_range_end))
        lines.append("fid_left_shift_phase0     : " + unicode(self.fid_left_shift_phase0))
        lines.append("ref_spectrum_source       : " + unicode(self.ref_spectrum_source))
        lines.append("ref_peak_line_width       : " + unicode(self.ref_peak_line_width))
        lines.append("constant_phase0_offset    : " + unicode(self.constant_phase0_offset))
        
        

        # __unicode__() must return a Unicode object. In practice the code
        # above always generates Unicode, but we ensure it here.
        return u'\n'.join(lines)


    def deflate(self, flavor=Deflate.ETREE):
        if flavor == Deflate.ETREE:
            e = ElementTree.Element("settings", {"version" : self.XML_VERSION})

            util_xml.TextSubElement(e, "fid_left_shift",        self.fid_left_shift)
            util_xml.TextSubElement(e, "gaussian_apodization",  self.gaussian_apodization)
            util_xml.TextSubElement(e, "global_phase1",         self.global_phase1)
            util_xml.TextSubElement(e, "apply_peak_shift",      self.apply_peak_shift)
            util_xml.TextSubElement(e, "reference_peak_center", self.reference_peak_center)
            util_xml.TextSubElement(e, "peak_search_width",     self.peak_search_width)
            util_xml.TextSubElement(e, "fid_left_shift_b0",     self.fid_left_shift_b0)
            util_xml.TextSubElement(e, "apply_phase0",          self.apply_phase0)
            util_xml.TextSubElement(e, "phase0_range_start",    self.phase0_range_start)
            util_xml.TextSubElement(e, "phase0_range_end",      self.phase0_range_end)
            util_xml.TextSubElement(e, "fid_left_shift_phase0", self.fid_left_shift_phase0)
            util_xml.TextSubElement(e, "ref_spectrum_source",   self.ref_spectrum_source)
            util_xml.TextSubElement(e, "ref_peak_line_width",   self.ref_peak_line_width)
            util_xml.TextSubElement(e, "constant_phase0_offset",   self.constant_phase0_offset)

            return e
            
        elif flavor == Deflate.DICTIONARY:
            return self.__dict__.copy()


    def inflate(self, source):
        if hasattr(source, "makeelement"):
            # Quacks like an ElementTree.Element

            for name in ("reference_peak_center", 
                         "gaussian_apodization", 
                         "peak_search_width", 
                         "global_phase1", 
                         'phase0_range_start', 
                         'phase0_range_end'):
                item = source.findtext(name)
                if item is not None:
                    setattr(self, name, float(item))

            for name in ("fid_left_shift", 
                         "fid_left_shift_b0",
                         "fid_left_shift_phase0", 
                         "ref_peak_line_width",
                         "constant_phase0_offset"):
                item = source.findtext(name)
                if item is not None:
                    setattr(self, name, int(item))

            for name in ("apply_peak_shift", 
                         "apply_phase0", ):
                item = source.findtext(name)
                if item is not None:
                    setattr(self, name, util_xml.BOOLEANS[item])

            for name in ("ref_spectrum_source",):
                item = source.findtext(name)
                if item is not None:
                    setattr(self, name, item)


        elif hasattr(source, "keys"):
            # Quacks like a dict
            for key in source.keys():
                if hasattr(self, key):
                    setattr(self, key, source[key])




class BlockPrepMegalaser(block_prep_identity.BlockPrepIdentity):
    """ 
    This is a building block object that can be used to create a list of
    processing blocks. 
    
    This object represents preprocessing of the raw data from the first 
    block ('raw') in the dataset.blocks list. 
    
    We sub-class from BlockPrepIdentity base class to minimize recreating
    wheels, but to also leave us the flexibility of extending this class 
    in the future for any 'special children' types of data loading.
    
    In here we also package all the functionality needed to save and recall
    these values to/from an XML node.

    """
    # The XML_VERSION enables us to change the XML output format in the future 
    XML_VERSION = "1.0.0"

    
    def __init__(self, attributes=None):
        """
        Here we set up the standard functionality of the base class
        
        """
        block_prep_identity.BlockPrepIdentity.__init__(self, attributes) 
        
        #----------------------------------------
        # processing parameters
        self.set = _Settings()


        #----------------------------------------
        # results storage

        self.frequency_shift = None
        self.phase_0 = None
        self.data = None
                                 
        if attributes is not None:
            self.inflate(attributes)

        self.chain = None


    ##### Standard Methods and Properties #####################################

#    # This overrides the data property from the Identity class which is read
#    # only. This form allows us to read/write
#    def __get_data(self):
#        return self._data
#    def __set_data(self, data):
#        self._data = data
#    data = property(__get_data, __set_data)



    @property
    def dims(self):
        """Data dimensions in a list, e.g. [1024, 1, 1, 1]. It's read only."""
        # Note that self.data.shape is a tuple. Dims must be a list.
        if self.data is not None:
            return list(self.data.shape[::-1])
        return None
        
        

    def __str__(self):
        return self.__unicode__().encode("utf-8")


    def __unicode__(self):
        lines = mrs_data_raw.DataRaw.__unicode__(self).split('\n')

        lines[0] = "----------- DataPrepMegalaser Object ------------"
        lines.append("Data shape                    : %s" % str(self.dims))

        return u'\n'.join(lines)


    def create_chain(self, dataset):
        self.chain = chain_prep_megalaser.ChainPrepMegalaser(dataset, self)


    def set_dims(self, dataset):
        """
        Given a Dataset object, this is an opportunity for this block object 
        to ensure that its dims match those of the parent dataset. 
        """
        block.Block.set_dims(self, dataset)

        # local reference to input data
        raw = dataset.get_source_data('prep')

        # this is the calculated proper size for self.data
        fidsum_dims = [raw.shape[-1],1,1,1]

        if not self.dims or self.dims != fidsum_dims: 
            self._reset_dimensional_data(dataset)


    def _reset_dimensional_data(self, dataset):
        """
        Resets (to zero) and resizes dimensionally-dependent data
        
        """
        # local reference to input data
        raw = dataset.get_source_data('prep')

        n_fids = raw.shape[-2]

        self.frequency_shift = np.zeros([n_fids])
        self.phase_0         = np.zeros([n_fids])

        self.data = np.zeros((1,1,1,raw.shape[-1]), dtype=raw.dtype)
        if self.chain is not None:
            self.chain.reset_results_arrays()
        
    
    def concatenate(self, new):
        raise NotImplementedError


    def deflate(self, flavor=Deflate.ETREE):
        if flavor == Deflate.ETREE:

            e = ElementTree.Element("block_prep_megalaser",
                                    { "id" : self.id,
                                      "version" : self.XML_VERSION})

            util_xml.TextSubElement(e, "behave_as_preset", self.behave_as_preset)
            
            # Now I deflate the attribs that are specific to this class
            e.append(self.set.deflate())
            
            if not self.behave_as_preset:

                e.append(util_xml.numpy_array_to_element(self.frequency_shift,'frequency_shift'))
                e.append(util_xml.numpy_array_to_element(self.phase_0,'phase_0'))
                e.append(util_xml.numpy_array_to_element(self.data, 'data'))

            return e

        elif flavor == Deflate.DICTIONARY:
            return self.__dict__.copy()


    def inflate(self, source):
        if hasattr(source, "makeelement"):

            val = source.findtext("behave_as_preset")   # default is False
            if val is not None:
                self.behave_as_preset = util_xml.BOOLEANS[val]

            # Quacks like an ElementTree.Element
            self.set = _Settings(source.find("settings"))

            if not self.behave_as_preset:
            
                # Now I inflate the attribs that are specific to this class
                temp = source.find("frequency_shift")
                self.frequency_shift = util_xml.element_to_numpy_array(temp)
                temp = source.find("phase_0")
                self.phase_0 = util_xml.element_to_numpy_array(temp)
                temp = source.find("data")
                self.data = util_xml.element_to_numpy_array(temp)


        elif hasattr(source, "keys"):
            # Quacks like a dict
            for key in source.keys():
                if key == "set":
                    setattr(self, key, source[key])


    ##### Private Methods #####################################

    
    
    
  
  
