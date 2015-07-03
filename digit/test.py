#!/usr/bin/python
from ABE_helpers import ABEHelpers
from ABE_IoPi import IoPi
import time
import os

import digit
"""
================================================
ABElectronics IO Pi 32-Channel Port Expander - Input Read Demo
Version 1.1 Created 30/04/2014
Version 1.2 changes to format source code to PEP8 rules 12/11/2014
Requires python smbus to be installed with: sudo apt-get install python-smbus
run with: sudo python demo-iopiread.py
================================================
This example reads the first 8 pins of bus 1 on the IO Pi board. The
internal pull-up resistors are enabled so each pin will read as 1 unless
the pin is connected to ground.
Initialise the IOPi device using the default addresses, you will need to
change the addresses if you have changed the jumpers on the IO Pi
"""
i2c_helper = ABEHelpers()
i2c_bus = i2c_helper.get_smbus()
multibus = [ IoPi(i2c_bus, 0x20), IoPi(i2c_bus, 0x21)]

d = digit.Digit(multibus,29)
while True:
	# clear the console
	os.system('clear')

	print 'Output: ' + str(d.read());
	time.sleep(0.1)

