#!/usr/bin/env python

# (c) 2016 Alexander Kahl <kahl@magneticcoffee.eu>

# Simple glob lookup


import glob
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        ret = []

        for term in terms:
            display.debug("Expanding glob term: %s" % term)

            for g in glob.glob(term):
                display.debug("Expanded to '%s'" % g)
                ret.append(g)
        return ret
