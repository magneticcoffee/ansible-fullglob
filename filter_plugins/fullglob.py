#!/usr/bin/env python

import glob

def fullglob(path):
    return glob.glob(path)


class FilterModule(object):
    ''' fullglob jinja2 filter '''

    def filters(self):
        return {
            'fullglob' : fullglob
        }
