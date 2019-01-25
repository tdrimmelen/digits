import json 
import serial
import ConfigParser 
import threading
import logging

class Scoreboardak30:
    empty=""
    def __init__(self, configfilename):
        
        config = ConfigParser.RawConfigParser()
        config.read(configfilename)
        port = config.get(self.__class__.__name__, 'port')
        baudrate = config.getint(self.__class__.__name__, 'baudrate')

        logging.debug(self.__class__.__name__ + ': Init with port: ' + port)
        logging.debug(self.__class__.__name__ + ': Init with baudrate: ' + str(baudrate))
        self.ser = serial.Serial(port=port, baudrate=baudrate)

        self.home = 0
        self.guest = 0
        self.minutes = 0
        self.seconds = 0
        self.period = 0

        self.status = True
        self.errorDetail = ''
        self.errorMessage = ''

        self.ser.flushInput()
        t1 = threading.Thread(target = self.readserial)
        t1.start()

    def readserial(self):
        while True:
            input = self.ser.readline()
            logging.debug('Value read from serial port: ' + input)

            try:
                self.minutes = int(input[20] + input[21])
                self.seconds = int(input[15] + input[14])
                self.home = int(input[17] + input[18] + input[19])
                self.guest = int(input[13] + input[12] + input[11])
                self.period = int(input[7])
                self.status = True
            except ValueError as e:
                self.status = False
                self.errorDetail = str(e)
                self.errorMessage = 'Error while parsing score/time'
                logging.error(self.__class__.__name__ + ': ValueError while reading input')

            
    def getJSONTime(self):
        if self.status:
            return json.dumps({'status' : 'OK', 'minute': self.minutes, 'second' : self.seconds, 'period': self.period})
        else:
            return json.dumps({'status' : 'Error', 'ErrorDetail' : self.errorDetail, 'ErrorMessage' : self.errorMessage})

    def getJSONScore(self):
        if self.status:
            return json.dumps({'status' : 'OK', 'home': self.home, 'guest' : self.guest})
        else:
            return json.dumps({'status' : 'Error', 'ErrorDetail' : self.errorDetail, 'ErrorMessage' : self.errorMessage})
