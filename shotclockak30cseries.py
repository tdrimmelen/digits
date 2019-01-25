import json 
import serial
import ConfigParser 
import threading
import logging

class Shotclockak30cseries:
    empty=""
    def __init__(self, configfilename):
        
        config = ConfigParser.RawConfigParser()
        config.read(configfilename)
        port = config.get(self.__class__.__name__, 'port')
        baudrate = config.getint(self.__class__.__name__, 'baudrate')

        logging.debug(self.__class__.__name__ + ': Init with port: ' + port)
        logging.debug(self.__class__.__name__ + ': Init with baudrate: ' + str(baudrate))
        self.ser = serial.Serial(port=port, baudrate=baudrate)

        self.time = 0

        self.status = True
        self.errorDetail = ''
        self.errorMessage = ''

        self.ser.flushInput()
        t1 = threading.Thread(target = self.readserial)
        t1.start()

    def readserial(self):
        while True:
            input = self.ser.readline()
            logging.debug(self.__class__.__name__ + ': Value read from serial port: ' + input)

            try:
                self.time = int(input[1] + input[2])
                self.status = True
            except ValueError as e:
                self.status = False
                self.errorDetail = str(e)
                self.errorMessage = 'Error while parsing time'
                logging.error(self.__class__.__name__ + ': ValueError while reading time')
            
    def getJSONTime(self):
        if self.status:
            return json.dumps({'status' : 'OK', 'time': self.time})
        else:
            return json.dumps({'status' : 'Error', 'ErrorDetail' : self.errorDetail, 'ErrorMessage' : self.errorMessage})


