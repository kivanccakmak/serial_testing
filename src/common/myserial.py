#!/usr/bin/python
import serial
import time

SERIAL_DUMMY_READ_COUNT = 10000000        #to avoid nulls in serial
SERIAL_READ_ONCE_LIMIT = 10000

class MySerial(object):
    
    """Serial Port Connection Supplier"""

    def __init__(self, port, timeout, baudrate, fields):
        """Constructor Method
        :port: str
        :timeout: int
        :baudrate: int
        :fields: dict
            additional meta data
        """
        self.port = port
        self.timeout = timeout
        self.baudrate = baudrate
        self.fields = fields
        self.session = None
        self.connect()

    def connect(self):
        """Initialize Serial Connection"""
        print("init serial on {}".format(str(self.port)))
        try:
            dev = serial.Serial(port=self.port,
                                baudrate=self.baudrate,
                                timeout=self.timeout)
        except:
            print("failed to init serial with {}".format(str(self.port)))
            return
        print("connected with {}".format(str(self.port)))
        self.session = dev

    def exec_command(self, cmd, read_limit=None):
        """run commands or single command
        :cmd: str or str[]
        :read_limit: int
        """
        if read_limit == None:
            read_limit == 1000000
        if type(cmd) == list:
            for cmd_str in cmd:
                out = self.__command(cmd_str, read_limit)
                time.sleep(1)
        elif type(cmd) == str:
            out = self.__command(cmd, read_limit)
        return out

    def __command(self, cmd, read_limit):
        """write command on serial port
        :cmd: str
        :return: str
            output of screen
        """
        byte_num = 0
        tmp = ''
        out = ''

        print(cmd)
        self.session.read(SERIAL_DUMMY_READ_COUNT)

        cmd += '\n'
        self.session.write(cmd)

        if read_limit == None:
            read_limit = SERIAL_READ_ONCE_LIMIT

        if read_limit > SERIAL_READ_ONCE_LIMIT:
            for _ in range(0, read_limit/SERIAL_READ_ONCE_LIMIT):
                tmp = self.session.read(SERIAL_READ_ONCE_LIMIT)
                out += tmp
                byte_num += len(tmp)
                if tmp == '':
                    break
        else:
            out = self.session.read(SERIAL_READ_ONCE_LIMIT)

        print("read {} bytes".format(byte_num))
        return out
