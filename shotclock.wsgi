# Append current path to path.
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import shotclock
import testshotclock
import logging
import logging.config
import json


# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/time')
def shotclocktime():

	try:
		logging.info('shotclockpath() start')
		time = s.getJSONTime()
		logging.info('shotclockpath() end')
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

	return ts.getJSONTime()


s = shotclock.Shotclock(os.path.dirname(__file__) + '/digits.cfg')
ts = testshotclock.Testshotclock()

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config
logging.info('Started')
application = bottle.default_app()
