import os
import sys
import ast
from common.common import get_config

CONFIG_FILE = 'config.ini'
EXIT_CODES = {'CONFIG_READ_ERROR': 2, 'MODULE_LOAD_ERROR': 3, 
        'FAILED_TEST': 1, 'SUCCESS': 0}

def get_test_suit(conf_file):
    """
    :conf_file: Str
    :return: Str[]
        list of modules to run in config file on success
        None on fail
    """
    config =  get_config(conf_file, ['test'])
    if config == None:
        print('failed to get config')
        return None

    if 'test' not in config.keys():
        print('invalid config file format [no test field]')
        return None

    if 'suite' not in config['test'].keys():
        print('invalid config file format [no suite field]')
        return None

    try:
        suit = ast.literal_eval(config['test']['suite'])
    except TypeError as e:
        print('failed to load suite')
        print('error message: {}'.format(e))
        return None

    return suit

def load_test_suit(test_suit):
    """
    :test_suit: Str[]
        list of modules to run
    :return: Bool
        False if any load operation fails
    """
    for elem in test_suit:
        print('loading {}'.format(elem))
        try:
            exec('import {}'.format(elem))
        except ImportError as e:
            print('failed to load {}'.format(elem))
            print('error message: {}'.format(e))
            return False
    return True

def run_all(test_suit):
    """
    :test_suit: String[]
    :return: Bool
        False if any test case fail
    """
    print('running all')
    for modname in test_suit:
        mod = sys.modules[modname]

        config = mod.__dict__['read_config']()
        if config is None:
            print('no config found for {}'.format(modname))
            return False

        if not mod.__dict__['run'](config):
            print('failed test')
            return False
    return True

def main():
    """
    """
    if not os.path.isfile(CONFIG_FILE):
        print('can not found {}'.format(CONFIG_FILE))
        sys.exit(EXIT_CODES['CONFIG_READ_ERROR'])

    modnames = get_test_suit(CONFIG_FILE)
    if not load_test_suit(modnames):
        print('failed to load test_suit: {}'.format(modnames))
        sys.exit(EXIT_CODES['MODULE_LOAD_ERROR'])

    if not run_all(modnames):
        sys.exit(EXIT_CODES['FAILED_TEST'])

    sys.exit(EXIT_CODES['SUCCESS'])

if __name__ == "__main__":
    sys.path.append(os.path.abspath('common'))
    main()
