from digit.digit import Digit
from time import sleep
from ABE_helpers import ABEHelpers
from ABE_IoPi import IoPi
import json
import logging
import ConfigParser

class Timeclock:

	def __init__(self, configfilename):

		config = ConfigParser.RawConfigParser()
		config.read(configfilename)
		inverted_logic = config.getboolean(self.__class__.__name__, 'inverted_logic')

		i2c_helper = ABEHelpers()
		i2c_bus = i2c_helper.get_smbus()
		multibus = [ IoPi(i2c_bus, 0x20), IoPi(i2c_bus, 0x21)]

		self.tenminute = Digit(multibus, 1, inverted_logic)
		self.minute = Digit(multibus, 8, inverted_logic)
		self.tensecond = Digit(multibus, 17, inverted_logic)
		self.second = Digit(multibus, 24, inverted_logic)
	
	def getJSONTime(self):

		# Try 2 times as it can return ValueError if time is changing
		for i in range(1,2):
			try:
				tenminute = self.tenminute.read() *10 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				minute = self.minute.read() 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				tensecond = self.tensecond.read() *10 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				second = self.second.read()
				return json.dumps({'status' : 'OK', 'minute': tenminute + minute, 'second' : tensecond + second})

			except ValueError as e:

				sleep(0.01)
				continue

		return json.dumps({'status' : 'Error', 'ErrorDetail' : str(e), 'ErrorMessage' : 'No valid time read' })

