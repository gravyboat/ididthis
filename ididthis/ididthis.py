#!/usr/bin/python

from __future__ import absolute_import
import os
import yaml
from ididthis.logging import local_logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def read_config(*kwargs):
    '''
    Read the default or user specific config file
    '''
    default_conf_options = {
            'local_log_dir': 'log',
            'local_log_file': 'ididthis.log',
            }

    if not kwargs:
        kwargs = {}

    if 'custom_root_dir' in kwargs:
        config_root_dir = custom_root_dir
    else:
        config_root_dir = root_dir
        
    ididthis_config = yaml.safe_load(open(config_root_dir + '/conf/ididthis.conf'))

    for conf_option, option_value in default_conf_options.items():
        if conf_option not in ididthis_config:
            ididthis_config.update({conf_option: option_value})

    return(ididthis_config)


def write_entry(ididthis_config, commit_message):
    '''
    Write a local entry to the specific config file
    '''

    if commit_message == '':
        print('A message to commit is required.')
        return(False)


    log_file = root_dir + '/' + ididthis_config['local_log_dir'] + '/' + ididthis_config['local_log_file']
    # move this to logging functions
    if not os.path.exists(os.path.dirname(root_dir + '/' + ididthis_config['local_log_dir'])):
        os.makedirs(os.path.dirname(root_dir + '/' + ididthis_config['local_log_dir']))

    open_log_file = open(log_file, 'a+')
    open_log_file.write(commit_message)
    open_log_file.close()


def write_entry_remotely(ididthis_config, commit_message):
    return(True)


def append_entry(ididthis_config, **kwargs):
    '''
    Modify a specific entry in the config, date and entry must be specified
    '''

    if not kwargs:
        kwargs = {}

    if 'date' and 'entry' not in kwargs:
        print('A date and entry are required.')
        return(False)

    return(True)

def get_date(ididthis_config, **kwargs):
    '''
    Return details on the date so we know what to look for
    '''
    return(True)


def get_history(ididthis_config, **kwargs):
    '''
    reads the file with a specific date where entry and date are in the command
    defaults to last 7 days (if they exist) and let users see specific entries
    if they need to modify them
    '''
    return(True)

#    return(result)
