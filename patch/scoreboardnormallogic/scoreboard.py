from digit.digit import Digit
from time import sleep
from ABE_helpers import ABEHelpers
from ABE_IoPi import IoPi
import json
import logging

class Scoreboard:

	def __init__(self):

		i2c_helper = ABEHelpers()
		i2c_bus = i2c_helper.get_smbus()
		multibus = [ IoPi(i2c_bus, 0x22), IoPi(i2c_bus, 0x23)]

		self.tenhome = Digit(multibus, 1)
		self.home = Digit(multibus, 8)
		self.tenguest = Digit(multibus, 17)
		self.guest = Digit(multibus, 24)
	
	def getJSONScore(self):

		# Try 2 times as it can return ValueError if time is changing
		for i in range(1,2):
			try:
				tenhome = self.tenhome.read() *10 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				home = self.home.read() 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				tenguest = self.tenguest.read() *10 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				guest = self.guest.read()
				return json.dumps({'status' : 'OK', 'home': tenhome + home, 'guest' : tenguest + guest})

			except ValueError as e:

				sleep(0.01)
				continue

		return json.dumps({'status' : 'Error', 'ErrorDetail' : str(e), 'ErrorMessage' : 'No valid score read' })

