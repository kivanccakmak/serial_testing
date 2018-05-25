import sys
import ast
from common.common import get_config

# TODO: read this from config file
def get_test_suit():
    """
    """
    config =  get_config('config.ini', ['test'])
    return ast.literal_eval(config['test']['suite'])

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
        config = mod.__dict__['get_config']()
        print(config)
        mod.__dict__['get_config']()

def main():
    """
    """
    modnames = get_test_suit()
    if not load_test_suit(modnames):
        print('failed to load test_suit: {}'.format(modnames))
        sys.exit(1)
    run_all(modnames)

if __name__ == "__main__":
    main()
