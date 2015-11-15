from nose.tools import *
import sys
import os
from ididthis import ididthis
from ididthis.logging import local_logging

def setup():
    '''
    Create our test config files
    '''
    with open('ididthis.conf', 'w') as conf_file:
        conf_file.write("#####2015-11/14######\n")
    conf_file.close()


def test_local_conf_read():
    '''
    Test reading from the local conf
    '''


def test_log_path():
    '''
    Test that the log pathing works
    '''
    log_path = ididthis.read_config()
    print(log_path)
    assert_equal(log_path, {'local_log_dir': './log',
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
    print("log write")


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
    os.remove('ididthis.conf')

