import json 
import serial
import ConfigParser 
import threading

class ScoreboardAK30:
    empty=""
    def __init__(self, configfilename):
        
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=19200)

        self.home = 0
        self.guest = 0
        self.minutes = 0
        self.seconds = 0
        self.period = 0

        self.ser.flushInput()
        t1 = threading.Thread(target = self.readserial)
        t1.start()

    def readserial(self):
        while True:
            input = self.ser.readline()

            self.minutes = int(input[19] + input[20])
            self.seconds = int(input[14] + input[13])
            self.home = int(input[16] + input[17] + input[18])
            self.guest = int(input[12] + input[11] + input[10])
            self.period = int(input[6])

            
    def getJSONTime(self):
        return json.dumps({'status' : 'OK', 'minute': self.minutes, 'second' : self.seconds, 'period': self.period})

    def getJSONScore(self):
        return json.dumps({'status' : 'OK', 'home': self.home, 'guest' : self.guest})

    def inError(self, error):
        self.error = error
