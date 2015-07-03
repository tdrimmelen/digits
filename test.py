#!/usr/bin/python
import time
import os

import testschotklok
import logging
import logging.config

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

logging.config.fileConfig('logger.cfg') #logfile config
logging.info('Started')

d = testschotklok.Testschotklok()
while True:
	# clear the console
	os.system('clear')

	print 'Output: ' + d.getJSONTime();
	time.sleep(0.1)

