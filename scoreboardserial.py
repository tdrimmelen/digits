import json 
import serial
import ConfigParser 
import threading

class Scoreboardserial:
    empty=""
    def __init__(self, configfilename):
        
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=19200)
        self.home = ""
        self.guest = ""
        self.minutes = ""
        self.seconds = ""
        self.buffer = ""
        self.error = False
        self.ser.flushInput()
        t1 = threading.Thread(target = self.readserial)
        t1.start()

    def readserial(self):
        while True:
            if (self.error):       
                return json.dumps({'status' : 'Error', 'ErrorDetail' : 'Testerror', 'ErrorMessage' : 'No valid time read' })
            rcv = self.ser.read(1)
            for i in rcv:
                if i==0:
                    pass
                elif i=="{":
                    self.buffer=i
                elif i=="}":
                    if self.buffer[6:11]=="D000B":
                        if len(self.buffer) > 22:
                           if ord(self.buffer[22]) > 128:
                              self.minutes = self.buffer[21]+chr(ord(self.buffer[22])-128)
                           else:
                              self.minutes = self.buffer[21]+self.buffer[22]
                           self.seconds = self.buffer[23:25]
                           self.home    = self.buffer[19:21]
                           self.guest   = self.buffer[16:18]
                    elif self.buffer[6:11]=="D0007":
                           self.home    = self.buffer[15:17]
                    elif self.buffer[6:11]=="D000A":
                           self.guest   = self.buffer[15:17]
					
                    # altijd leegmaken					
                    self.buffer=self.empty
                else:
                    self.buffer=self.buffer+i
       
            
    def getJSONTime(self):
        return json.dumps({'status' : 'OK', 'minute': self.minutes, 'second' : self.seconds})
    def getJSONScore(self):
        return json.dumps({'status' : 'OK', 'home': self.home, 'guest' : self.guest})
    def inError(self, error):
        self.error = error
