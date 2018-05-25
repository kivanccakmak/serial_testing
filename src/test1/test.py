import os
import sys
from common.common import get_config
from common.common import get_slave_names

CONFIG_PATH=os.path.abspath('test1/config.ini')

def read_config():
    """
    :return: dict
        None in fail
    """
    global CONFIG_PATH
    section = ['test', 'timeouts', 'gw']
    slave_names = get_slave_names(CONFIG_PATH)
    section += slave_names
    config = get_config(CONFIG_PATH, section)
    return config

def run(config):
    """
    :config: dict
    :return: Bool
        False on fail, True on positive
    """
    print(config)
    return True
