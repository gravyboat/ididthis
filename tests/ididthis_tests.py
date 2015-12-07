from nose.tools import *
import sys
import os
import errno
from ididthis import ididthis
from ididthis.logging import local_logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def setup():
    '''
    Create our test log file and conf file
    '''
    if not os.path.exists(os.path.dirname(root_dir + '/log/')):
        try:
            os.makedirs(os.path.dirname(root_dir + '/log/'))
        except OSError as system_error:
            if system_error.errno != errno.EEXIST:
                raise system_serror
            pass

    with open(root_dir + '/log/ididthis.log', 'w') as log_file:
        log_file.write("#####2015-11-[23-29]######\n")
    log_file.close()

    if not os.path.exists(os.path.dirname(root_dir + '/tests/conf/ididthis.conf')):
        try:
            os.makedirs(os.path.dirname(root_dir + '/tests/conf/'))
        except OSError as system_error:
            if system_error.errno != errno.EEXIST:
                raise system_serror
            pass
    with open(root_dir + '/tests/conf/ididthis.conf', 'w') as conf_file:
        conf_file.write("local_log_dir: log_test\nlocal_log_file: ididthis.log")
    conf_file.close()


def test_local_conf_read():
    '''
    Test reading from the local conf even though we do it elsewhere
    '''
    test_conf_read = ididthis.read_config()
    assert_equal(test_conf_read, {'local_log_dir': 'log',
                            'local_log_file': 'ididthis.log'}
                )

def test_custom_conf_dir():
    '''
    Test out a different root dir, will eventually be a command
    line option
    '''
    custom_conf_dir = (root_dir + '/tests')
    test_custom_conf_dir = ididthis.read_config()
    # While file is written something is wrong with logic here, not reading file
    assert_equal(test_custom_conf_dir, {'local_log_dir': 'log',
                            'local_log_file': 'ididthis.log'}
                )


def test_log_path():
    '''
    Test that the log pathing is accurate
    '''
    # Right now this does the same thing as local_conf_read
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


def test_remote_log_write():
    '''
    Test writing to a remote location
    '''
    log_path = ididthis.read_config()
    commit_message = 'i did this'
    assert_true(ididthis.write_entry_remotely(log_path, commit_message))


def test_log_history():
    '''
    Test reading from the log
    '''
    log_path = ididthis.read_config()
    assert_true(ididthis.get_history(log_path))
    print("log read")


def test_log_history_specific_date():
    '''
    Test reading a specific date from the log
    '''
    pass
    

def test_append_entry():
    '''
    Test appending an entry
    '''
    log_path = ididthis.read_config()
    assert_true(ididthis.append_entry(log_path, date='test', entry='test'))


def test_no_append_entry():
    '''
    Test appending an entry with no data
    '''
    log_path = ididthis.read_config()
    assert_false(ididthis.append_entry(log_path))


def test_get_date():
    log_path = ididthis.read_config()
    assert_true(ididthis.get_date(log_path))


def teardown():
    '''
    Delete our test config files
    '''
    os.remove(root_dir + '/log/ididthis.log')
    os.rmdir(root_dir + '/log')

