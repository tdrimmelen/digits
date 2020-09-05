import json 
import serial
import ConfigParser 
import threading
import logging

class Scoreboardwesterstrandbasic200250:
    empty=""
    def __init__(self, configfilename):
        
        config = ConfigParser.RawConfigParser()
        config.read(configfilename)
        port = config.get(self.__class__.__name__, 'port')
        baudrate = config.getint(self.__class__.__name__, 'baudrate')

        logging.debug(self.__class__.__name__ + ': init with port: ' + port)
        logging.debug(self.__class__.__name__ + ': init with baudrate: ' + str(baudrate))
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
            c = self.ser.read(1)
            response += c
            try:
                if not ord(response[-1:]) is 2:        
                    continue
                       
                if len(response) < 5:
                    response = ''
                    continue
                # time
                if response[4] is '!':
                    self.minutes = int(response[6] + response[7])
                    self.seconds = int(response[8] + response[9])
                if response[4] is '#':
                    self.home = int(response[6] + response[7])
                    self.guest = int(response[10] + response[11])    
                if response[4] is '%' and ord(response[5]) is 32:
                    self.period = int(response[6])
            except:
                print("Error parsing score from line: " + response)
            response = ''

            
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
