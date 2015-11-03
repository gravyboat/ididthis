#!/usr/bin/python

import os
import yaml
from optparse import OptionParser
from .logging import local_logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def read_config(kwargs=None):

    default_conf_options = {
            'local_log_dir': './log',
            'local_log_file': 'ididthis.log',
            }

    ididthis_config = yaml.safe_load(open(root_dir + '/conf/ididthis.conf'))

    if not ididthis_config:
        ididthis_config = {}

    for conf_option, option_value in default_conf_options.items():
        if conf_option not in ididthis_config:
            ididthis_config.update({conf_option: option_value})

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
