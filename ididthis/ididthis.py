#!/usr/bin/python

import os
import yaml
from optparse import OptionParser
from .logging import local_logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def read_config(kwargs=None):

    ididthis_config = yaml.safe_load(open(root_dir + '/conf/ididthis.conf'))
    print(ididthis_config)
    return(ididthis_config)

def get_history(kwargs=None):

    return(result)

def write_entry(kwargs=None):

    return(result)


if __name__ == '__main__':
   read_config() 
'''
    parser = OptionParser()
    parser.add_option()
    parser.add_option()
    parser.add_option()

    (options, args) = parser.parse_args()
'''
