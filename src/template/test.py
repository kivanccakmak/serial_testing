import os
import sys
from common.common import get_config
from common.common import get_slave_names

CONFIG_PATH=os.path.abspath('template/config.ini')

# API functions
def read_config():
    """
    :return: dict
        None in fail
    """
    config = get_config(CONFIG_PATH, ['parameters'])
    return config

def run(config):
    """
    :config: dict
    :return: Bool
        False on fail, True on positive
    """
    return do_test(config)

# Private functions
def do_test(config):
    """
    :config: Dict
    :return: Bool
    """
    print(config)
    params = config['parameters']

    for i in range(0, int(params['trial'])):
        print('try counter {}'.format(i))
    print('dummy test passed')
    return True
