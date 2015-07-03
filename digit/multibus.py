class Multibus:

	PINCOUNT = 16

	def __init__(self, buslist):
        	self.buslist = buslist

	
	# throw ValueError when not found
	# read pin. Pin 1 to 16 is from bus 1, 2 to 32 from bus 2 etc.
	def read_pin(self,pin):

		bus = self.buslist[ ( pin - 1) // self.PINCOUNT]

		return bus.read_pin( ( ( pin - 1 ) % self.PINCOUNT ) + 1)

