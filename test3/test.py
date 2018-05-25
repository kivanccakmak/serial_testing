#!/usr/bin/python
import os
import sys
import time
import pyping

from myserial import MySerial
from common import get_slave_names, get_config

def get_config():
    """
    :return: dict
        None in fail
    """
    section = ['test', 'timeouts', 'gw']
    slave_names = get_slave_names("config.ini")
    section += slave_names
    config = get_config("config.ini", section)
    return config

def run(config):
    """
    :config: dict
    :return: Bool
        False on fail, True on positive
    """
    gw, slaves = initialize(config, slave_names)
    return rm_req_test(gw, slaves, config)

def rm_req_test(gw, slaves, config):
    """
    :gw: MySerial
    :slaves: MySerial[]
    :config: dict
    :return: Bool
        False on fail, True on positive
    """
    restart(slaves, "reboot")
    print("sleep({})".format(config['timeouts']['init']))
    time.sleep(int(config['timeouts']['init']))

    for i in range(0, int(config['test']['num_trial'])):
        if can_ping_node(gw.fields['ip']):
            print("success")
        else:
            print("fail")
            return False

        for slave in slaves:
            if can_ping_node(slave.fields['ip']):
                print("success")
            else:
                print("fail")
        restart(slaves, "reboot")
        print("sleep({})".format(config['timeouts']['reboot']))
        time.sleep(int(config['timeouts']['reboot']))
    return True

def can_ping_node(ip_addr):
    """
    :ip_addr: Str
    :return: Bool
    """
    r = pyping.ping(ip_addr)
    if r.ret_code == 0:
        return True
    return False 

def restart(nodes, cmd):
    """
    :nodes: MySerial[]
    :cmd: String
        has to be either "reboot" or "defaults"
        default value is "reboot"
    """
    if cmd == None:
        cmd="reboot"

    if cmd not in ["reboot", "defaults"]:
        print("invalid cmd{}".format(cmd))
        return

    for node in nodes:
        node.exec_command(cmd)

def initialize(config, slave_names):
    """
    :config: dict
    :slave_names: Str
        [new0, new1, ...]
    :return: MySerial, MySerial[]
        gw, slaves[]
    """
    gw, slaves = None, []

    gw = MySerial(
            config['gw']['tty'],
            int(config['gw']['timeout']),
            int(config['gw']['baudrate']),
            {
                'ip':config['gw']['ip'],
            }
            )
    time.sleep(1)

    for name in slave_names:
        slaves.append(
            MySerial(
                config[name]['tty'],
                int(config[name]['timeout']),
                int(config[name]['baudrate']),
                {
                    'ip':config[name]['ip'],
                }
                )
            )
        time.sleep(1)

    return gw, slaves
