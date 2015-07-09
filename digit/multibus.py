import logging

class Multibus:

	PINCOUNT = 16
	PINSPERPORT = 8

	"""
	bus 0           bus 1
	pin 0   port 1  port 0  port 1
	|-------|-------|-------|-------
	1       8       16      24
        pin
	"""

	def __init__(self, buslist):
        	self.buslist = buslist

	
	# throw ValueError when not found
	# read pin. Pin 1 to 16 is from bus 1, 2 to 32 from bus 2 etc.
	def read_pin(self,pin):

		bus = self.buslist[ ( pin - 1) // self.PINCOUNT]

		return bus.read_pin( ( ( pin - 1 ) % self.PINCOUNT ) + 1)

	def read_byte(self,start):

		#startport is port where first part of byte is read from
		startport = ( start - 1 ) // self.PINSPERPORT
		startport = startport % (self.PINCOUNT / self.PINSPERPORT) 
		logging.debug('Startport: ' + str(startport))

		#startbus is bus where first part of byte is read from
		startbus = ( start - 1) // self.PINCOUNT
		logging.debug('Startbus: ' + str(startbus))

		#startpin is pin where byte read start from
		startpin = ( ( start- 1 ) % self.PINSPERPORT ) + 1
		logging.debug('Startpin: ' + str(startpin))

		value = (self.buslist[ startbus ]).read_port( startport )
		logging.debug('Value: ' + str(value))

		if ( startpin > 1 ):

			#read value from next port in row
			value2 = (self.buslist[startbus + startport]).read_port(1 - startport)
			logging.debug('Value2: ' + str(value2))

			"""
			Example
			|-------|------
			   ********
			5 bits are read from start port, 2 bits from next port
			5 bits needs to be shifters
			"""
			#move read value to start
			value = value >> (startpin - 1) 
			logging.debug('Value shifted: ' + str(value))

			value2 = ( value2 << (8 - ( startpin - 1 ) ) ) % 256
			logging.debug('Value2 shifted: ' + str(value2))

			value = value + value2

		logging.debug('Return: ' + str(value))
		return value


