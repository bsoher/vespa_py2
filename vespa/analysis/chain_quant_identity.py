# Python modules
from __future__ import division

# 3rd party modules

# Our modules
import vespa.analysis.chain_base as chain_base


class ChainQuantIdentity(chain_base.Chain):
    # FIXME PS docstring
    def __init__(self, dataset, block):
        """ Prepare the base class. """
        chain_base.Chain.__init__(self, dataset, block)

        
