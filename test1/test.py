import os

def get_config():
    """
    :return: dict
        None in fail
    """
    return {'a':'1', 'b':'2'}

def run(config):
    """
    :config: dict
    :return: Bool
        False on fail, True on positive
    """
    print(config)
    return True
