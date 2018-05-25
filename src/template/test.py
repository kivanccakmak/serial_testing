import os
import sys
from common.common import get_config
from common.common import get_slave_names

CONFIG_PATH=os.path.abspath('template/config.ini')

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
    print(config)
    return True
