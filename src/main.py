import os
import sys
import ast
from common.common import get_config

def get_test_suit():
    """
    :return: String[]
        None on fail
    """
    config =  get_config('config.ini', ['test'])
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
    """
    print('running all')
    for modname in test_suit:
        mod = sys.modules[modname]
        config = mod.__dict__['read_config']()
        mod.__dict__['run'](config)

def main():
    """
    """
    if not os.path.isfile('config.ini'):
        print('can not found config.ini')
        sys.exit(1)

    modnames = get_test_suit()
    if not load_test_suit(modnames):
        print('failed to load test_suit: {}'.format(modnames))
        sys.exit(1)

    run_all(modnames)

if __name__ == "__main__":
    sys.path.append(os.path.abspath('common'))
    main()
