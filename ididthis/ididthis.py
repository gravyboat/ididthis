#!/usr/bin/python

from __future__ import absolute_import
import os
import yaml
from optparse import OptionParser
from ididthis.logging import local_logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def read_config(kwargs=None):
    '''
    Read the default or user specific config file
    '''
    default_conf_options = {
            'local_log_dir': 'log',
            'local_log_file': 'ididthis.log',
            }

    if not kwargs:
        kwargs = {}

    if 'root_dir' in kwargs:
        print('Custome root dir')

    ididthis_config = yaml.safe_load(open(root_dir + '/conf/ididthis.conf'))

    if not ididthis_config:
        ididthis_config = {}

    for conf_option, option_value in default_conf_options.items():
        if conf_option not in ididthis_config:
            ididthis_config.update({conf_option: option_value})

    return(ididthis_config)


def write_entry(ididthis_config, commit_message):
    '''
    Write a local entry to the specific config file
    '''

    if not commit_message:
        print('A message to commit is required.')
        return(False)


    log_file = root_dir + '/' + ididthis_config['local_log_dir'] + '/' + ididthis_config['local_log_file']
    # move this to logging functions
    if not os.path.exists(os.path.dirname(root_dir + '/' + ididthis_config['local_log_dir'])):
        os.makedirs(os.path.dirname(root_dir + '/' + ididthis_config['local_log_dir']))

    open_log_file = open(log_file, 'a+')
    open_log_file.write(commit_message)
    open_log_file.close()


def write_entry_remotely(ididthis_config, kwargs=None):
    pass


def append_entry(ididthis_config, kwargs=None):
    '''
    Modify a specific entry in the config, date and entry must be specified
    '''

    if not kwargs:
        kwargs = {}

    if 'date' and 'entry' not in kwargs:
        print('A date and entry are required.')
        return(False)

def get_date(ididthis_config, kwargs=None):
    pass


def get_history(ididthis_config, kwargs=None):
    '''
    reads the file with a specific date where entry and date are in the command
    defaults to last 7 days (if they exist) and let users see specific entries
    if they need to modify them
    '''

#    return(result)



if __name__ == '__main__':
    ididthis_config = read_config()

    parser = OptionParser()
    parser.add_option("-r",
                      "--remote",
                      dest = "remote",
                      help = "Log entry remotely"
                     )
    parser.add_option("-c",
                      "--config",
                      dest = "config",
                      help = "Specify config location"
                     )
    parser.add_option("-g",
                      "--get-history",
                      dest = "get_history",
                      help = "Get your history, time range can be integer"
                     )

    (options, args) = parser.parse_args()
