# Python modules
from __future__ import division

# 3rd party modules

# Our modules
#import vespa.common.util.import_ as common_util_import

from vespa.common.util.import_ import Importer

import vespa.analysis.mrs_dataset as mrs_dataset
import vespa.common.mrs_prior as mrs_prior
import vespa.common.mrs_data_raw as mrs_data_raw


class DatasetImporter(Importer):
    def __init__(self, source):
        Importer.__init__(self, source, None, False)

    def go(self, add_history_comment=False):
        for element in self.root.getiterator("dataset"):
            self.found_count += 1

            dataset = mrs_dataset.Dataset(element)
            
            self.imported.append(dataset)

        self.post_import()
        
        return self.imported


class DatasetCliImporter(Importer):
    def __init__(self, source):
        Importer.__init__(self, source, None, False)

    def go(self, add_history_comment=False):
        for element in self.root.getiterator("dataset"):
            self.found_count += 1

            dataset = mrs_dataset.Dataset(element)
            
            self.imported.append(dataset)

        self.post_import()
        
        return self.imported, self.timestamp
    

class DataRawImporter(Importer):
    def __init__(self, source):
        Importer.__init__(self, source, None, False)

    def go(self, add_history_comment=False):
        for element in self.root.getiterator("data_raw"):
            self.found_count += 1

            data = mrs_data_raw.DataRaw(element)
            
            self.imported.append(data)

        self.post_import()
        
        return self.imported
    

class PriorImporter(Importer):
    def __init__(self, source):
        Importer.__init__(self, source, None, False)


    def go(self, add_history_comment=False):
        for element in self.root.getiterator("prior"):
            self.found_count += 1

            prior = mrs_prior.Prior(element)

            self.imported.append(prior)

        self.post_import()
        
        return self.imported
