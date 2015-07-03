import multibus
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

	ZERO =  [1,1,1,0,1,1,1]
	ONE =   [0,0,1,0,0,1,0]
	TWO =   [1,0,1,1,1,0,1]
	THREE = [1,0,1,1,0,1,1]
	FOUR =  [0,1,1,1,0,1,0]
	FIVE =  [1,1,0,1,0,1,1]
	SIX =   [1,1,0,1,1,1,1]
	SEVEN = [1,0,1,0,0,1,0]
	EIGHT = [1,1,1,1,1,1,1]
	NINE = 	[1,1,1,1,0,1,1]

	DIGITMAP = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

	def __init__(self, mb, startpin):
        	self.multibus = multibus.Multibus(mb)
		self.startpin = startpin

		for bus in mb :
			bus.set_port_direction(0, 0xFF)
			bus.set_port_pullups(0, 0xFF)

			bus.set_port_direction(1, 0xFF)
			bus.set_port_pullups(1, 0xFF)

	# throw ValueError when not found
	def read(self):

		pin = []
		for x in range(self.startpin, ( self.startpin + self.SEGMENT_COUNT ) ) :
			value = self.multibus.read_pin(x)
			pin.append(value)
			logging.debug('Pin ' + str(x) + ' value: ' + str(value))

		return self.DIGITMAP.index(pin)

