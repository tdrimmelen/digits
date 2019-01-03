import json 
import serial
import ConfigParser 
import threading
import logging

class Shotclockc4:
    empty=""
    def __init__(self, configfilename):
        
        config = ConfigParser.RawConfigParser()
        config.read(configfilename)
        port = config.get(self.__class__.__name__, 'port')
        baudrate = config.getint(self.__class__.__name__, 'baudrate')

        self.ser = serial.Serial(port=port, baudrate=baudrate)

        self.time = 0

        self.ser.flushInput()
        t1 = threading.Thread(target = self.readserial)
        t1.start()

    def readserial(self):
        while True:
            input = self.ser.readline()
            logging.debug('Value read from serial port: ' + input)

            self.time = int(input[0] + input[1])
            
    def getJSONTime(self):
        return json.dumps({'status' : 'OK', 'time': self.time})

