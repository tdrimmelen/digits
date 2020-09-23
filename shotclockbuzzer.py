import logging
import buzzercontroller

class Shotclockbuzzer:

	def __init__(self):

		self.buzzer = buzzercontroller.buzzercontroller()
		self.hasBuzzed = False
	
	def playWhenNeeded(self, time):

		if (time == 0 and not self.hasBuzzed):

			self.buzzer.play()
			self.hasBuzzed = True
			
		if (time != 0):
	
			self.hasBuzzed = False
			
