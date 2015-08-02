from time import sleep, time
import json
import logging
import math

class Testscoreboard:

	def __init__(self):

		self.home = 0
		self.away = 0
		self.error = False

	def getJSONScore(self):

		if (self.error):

			return json.dumps({'status' : 'Error', 'ErrorDetail' : 'Testerror', 'ErrorMessage' : 'No valid score read' })

		return json.dumps({'status' : 'OK', 'home' : self.home , 'away' : self.away})

	def setScore(self, home, away):

		self.home = home
		self.away = away

	def inError(self, error):

		self.error = error
		
		

