from nose.tools import *
import sys
import os
from ididthis import ididthis
from ididthis.logging import local_logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def setup():
    '''
    Create our test log file and conf file
    '''
    if not os.path.exists(os.path.dirname(root_dir + '/log/ididthis.log')):
            os.makedirs(os.path.dirname(root_dir + '/log/ididthis.log'))
    with open(root_dir + '/log/ididthis.log', 'a') as log_file:
        log_file.write("#####2015-11-[23-29]######\n")
    log_file.close()


def test_local_conf_read():
    '''
    Test reading from the local conf
    '''

def test_custom_root_dir():
    '''
    Test out a different root dir, will eventually be a command
    line option
    '''
    custom_root_dir = ididthis.read_config(root_dir)
    assert_equal(custom_root_dir, {'local_log_dir': 'log',
                            'local_log_file': 'ididthis.log'}
                )


def test_log_path():
    '''
    Test that the log pathing works
    '''
    log_path = ididthis.read_config()
    print(log_path)
    assert_equal(log_path, {'local_log_dir': 'log',
                            'local_log_file': 'ididthis.log'}
                )

    
def test_custom_log_path():
    '''
    Test that the custom log pathing works
    '''
    print("Custom pathing")


def test_log_write():
    '''
    Test writing to the log file
    '''
    log_path = ididthis.read_config()
    commit_message = 'i did this'

    ididthis.write_entry(log_path, commit_message)
    print("log write")

def test_no_log_write():
    '''
    Test what happens when we try to write with no commit
    '''
    log_path = ididthis.read_config()
    commit_message = ''
    assert_false(ididthis.write_entry(log_path, commit_message))


def test_log_read():
    '''
    Test reading from the log
    '''
    print("log read")


def test_log_read_specific_date():
    '''
    Test reading a specific date from the log
    '''
    print("read specific date")


def teardown():
    '''
    Delete our test config files
    '''
#    os.remove(root_dir + '/log/ididthis.log')
    pass

