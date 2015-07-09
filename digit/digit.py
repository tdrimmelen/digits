from .multibus import Multibus
import logging

class Digit:

	PIN_INPUT = 1
	SEGMENT_COUNT = 7

	#Digit encoding, top to bottom, left to right
	#   0
	#   -
	# 1| |2
	#   -3
	# 4| |5
	#   -
	#   6

	ZERO = 0b01110111 # [1,1,1,0,1,1,1]
	ONE = 0b00100100  # [0,0,1,0,0,1,0]
	TWO = 0b01011101  #  [1,0,1,1,1,0,1]
	THREE = 0b01101101 # [1,0,1,1,0,1,1]
	FOUR = 0b00101110 # [0,1,1,1,0,1,0]
	FIVE = 0b01101011 # [1,1,0,1,0,1,1]
	SIX = 0b01111011 #  [1,1,0,1,1,1,1]
	SEVEN = 0b00100101 # [1,0,1,0,0,1,0]
	EIGHT = 0b01111111 # [1,1,1,1,1,1,1]
	NINE = 0b01101111 # 	[1,1,1,1,0,1,1]
	NOTH = 0b00000000 # [0,0,0,0,0,0,0]

	DIGITMAP = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, NOTH]

	def __init__(self, mb, startpin, invert=False):
		self.multibus = Multibus(mb)
		self.startpin = startpin

		for bus in mb :
			bus.set_port_direction(0, 0xFF)
			bus.set_port_pullups(0, 0x00)

			bus.set_port_direction(1, 0xFF)
			bus.set_port_pullups(1, 0x00)

			if invert :
				bus.invert_port(0, 1)
				bus.invert_port(1, 1)

	# throw ValueError when not found
	def read(self):

		pin = []
		value = self.multibus.read_byte(self.startpin)
		value = value & 0b01111111
		logging.debug('Value: ' + str(value))

		"""
		for x in range( 0, self.SEGMENT_COUNT ) :

			pinvalue = ( value & pow( 2, x) ) >> x 
			logging.debug('Pin ' + str(x) + ' value: ' + str(pinvalue))
			pin.append(pinvalue)
		"""

		return (self.DIGITMAP.index(value) % 10 )

