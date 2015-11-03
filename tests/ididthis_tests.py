from nose.tools import *
from ididthis import ididthis

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_log_path():
    log_path = ididthis.read_config()
    print(log_path)
    assert_equal(log_path, {'local_log_dir': './log'})

def test_local_log():
    print('yep!')

def test_base():
    print("I RAN!")
