#!/usr/bin/python
import ast
import ConfigParser

def get_slave_names(conf_file):
    """
    :conf_file: String
    :return: String[]
        [new0, new1, ...]
    """
    try:
        parser = ConfigParser.SafeConfigParser()
        parser.read(conf_file)
    except:
        print("could not parse {}".format(conf_file))
        sys.exit(1)

    test_conf = {}
    for name, val in parser.items('test'):
        test_conf[name] = val
    return ast.literal_eval((test_conf['slaves']))

def get_config(conf_file, sections):
    """
    :conf_file: String
    :sections: String[]
    :return: dict
    """
    config = {}
    try:
        parser = ConfigParser.SafeConfigParser()
        parser.read(conf_file)
    except:
        print("could not parse {}".format(conf_file))
        sys.exit(1)

    for elem in sections:
        config[elem] = {}
        for name, value in parser.items(elem):
            config[elem][name] = value
    return config
