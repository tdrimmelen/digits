from time import sleep, time
import json
import logging
import math

class Testscoreboard:

	def __init__(self):

		self.home = 0
		self.guest = 0
		self.error = False

	def getJSONScore(self):

		if (self.error):

			return json.dumps({'status' : 'Error', 'ErrorDetail' : 'Testerror', 'ErrorMessage' : 'No valid score read' })

		return json.dumps({'status' : 'OK', 'home' : self.home , 'guest' : self.guest})

	def setScore(self, home, guest):

		self.home = home
		self.guest = guest

	def inError(self, error):

		self.error = error
		
		

