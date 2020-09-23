# Append current path to path.
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import testshotclock
import logging
import logging.config
import json
import importlib
import ConfigParser 
import shotclockbuzzer

configFileName = os.path.dirname(__file__) + '/digits.cfg'

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/time')
def shotclocktime():

	try:
		logging.info('shotclocktime() start')
		time = s.getJSONTime()
		logging.info('shotclocktime() end')
		return time
	except:
		logging.exception('Uncaught exception')
		raise

@route('/time-as-array')
def shotclocktimeasarray():

	try:
		logging.info('shotclockyimeasarray() start')
		time = s.getJSONTime()
		data = json.loads(time)
		list= [data]
		time = json.dumps(list)
		logging.info('shotclocktimeasarray() end')
		return time
	except:
		logging.exception('Uncaught exception')
		raise

@route('/test/start', method='PUT')
def testshotclockStart():

	ts.start()
	return "Started"

@route('/test/stop', method='PUT')
def testshotclockStop():

	ts.stop()
	return "Stopped"

@route('/test/reset', method='PUT')
def testshotclockReset():

	ts.reset()
	return "Stopped"

@route('/test/inError', method='PUT')
def testshotclockinError():

	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('inError'):
		abort(400, 'No inError specified')
	error = entity['inError']
	ts.inError(error)

@route('/test/time')
def testshotclocktime():
	
	time = ts.getJSONTime()
	data = json.loads(time)

	if data['status'] == 'OK':
		buzzer.playWhenNeeded(data['time']) 

	return time

@route('/test/time-as-array')
def testshotclocktimeasarray():

	time = ts.getJSONTime()
	data = json.loads(time)
	list= [data]
	time = json.dumps(list)
	return time

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config

#Read shotclock from config file
config = ConfigParser.RawConfigParser()
config.read(configFileName)
type = config.get('Shotclock', 'type')

# Start the configured shotclock class
module = importlib.import_module(type)
class_ = getattr(module, type.capitalize())
s = class_(configFileName)

ts = testshotclock.Testshotclock()

buzzer = shotclockbuzzer.Shotclockbuzzer()

logging.info('Started')
application = bottle.default_app()
