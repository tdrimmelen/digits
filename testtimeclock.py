from time import sleep, time
import json
import logging
import math

class Testtimeclock:

	def __init__(self):

		self.time = 0.0
		self.run = False
		self.error = False

	def getJSONTime(self):

		if (self.error):

			return json.dumps({'status' : 'Error', 'ErrorDetail' : 'Testerror', 'ErrorMessage' : 'No valid time read' })

		if ( self.run ):
			elaptime = math.floor(self.time + time() - self.starttime)
		else:
			elaptime = math.floor(self.time)

		elaptime = max(0, 25*60 - elaptime)

		return json.dumps({'status' : 'OK', 'minute' : int(elaptime / 60) , 'second' : int(elaptime % 60)})

	def start(self):

		self.starttime = time()
		self.run = True

	def stop(self):

		self.time = self.time + time() - self.starttime
		self.run = False

	def reset(self):

                self.time = 0.0
                self.run = False

	def setTime(self, minute, second):

		self.time = 25*60 - minute*60.0 - second

	def inError(self, error):

		self.error = error
		
		

