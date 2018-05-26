#!/usr/bin/python
import ast
import ConfigParser
import os

def get_slave_names(conf_file):
    """
    :conf_file: String
    :return: String[]
        [new0, new1, ...]
    """
    test_conf = {}
    parser = ConfigParser.SafeConfigParser()

    if not os.path.isfile(conf_file):
        print('{} does not exist'.format(conf_file))
        return None

    try:
        parser.read(conf_file)
    except ParsingError as e:
        print("could not parse {}".format(conf_file))
        print('error message: {}'.format(e))
        return None

    for name, val in parser.items('test'):
        test_conf[name] = val
    return ast.literal_eval((test_conf['slaves']))

def get_config(conf_file, sections):
    """read sections in config file
    :conf_file: String
    :sections: String[]
    :return: dict
    """
    config = {}
    parser = ConfigParser.SafeConfigParser()

    if not os.path.isfile(conf_file):
        print('{} does not exist'.format(conf_file))
        return None

    try:
        out = parser.read(conf_file)
    except ParsingError as e:
        print("could not parse {}".format(conf_file))
        print('error message: {}'.format(e))
        return None

    for elem in sections:
        config[elem] = {}
        for name, value in parser.items(elem):
            config[elem][name] = value
    return config
