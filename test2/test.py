import os

def read_config():
    """
    :return: dict
        None in fail
    """
    return {'ax':'1', 'bx':'2'}

def run(config):
    """
    :config: dict
    :return: Bool
        False on fail, True on positive
    """
    print(config)
    return True
