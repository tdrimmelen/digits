import json 
import serial
import ConfigParser 
import threading
import logging
import io

class Scoreboardledyears3505:
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
        last_pressed = False
        response = ''
        while True:
            response += self.ser.read()
            if not response[-1:] is '}':
                continue

            input = [ord(c) for c in response]
            response = ''
            # if input[13] == 'p' (char 80) there is an update to the time / scoreboard
            if input[13] is 80:
                if input[10] is 52:
                    majorminute = str(chr(input[14]))
                    minorminute = hex(input[15])[-1:]
                    self.minutes = int(majorminute + minorminute)
                    self.seconds = int(str(chr(input[16])) + str(chr(input[17])))
                    print(str(self.minutes) + ':' + str(self.seconds))
                if input[10] is 65:
                    self.guest = int(chr(input[14]) + chr(input[15]) + chr(input[16]))
                if input[10] is 55:
                    self.home = int(chr(input[14]) + chr(input[15]) + chr(input[16]))

            
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
