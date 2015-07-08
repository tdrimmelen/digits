# Append current path to path.
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import schotklok
import testschotklok
import logging
import logging.config
import json


# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/time')
def schotkloktime():

	try:
		logging.debug('schotklokpath() start')
		time = s.getJSONTime()
		logging.debug('schotklokpath() end')
		return time
	except:
		logging.exception('Uncaught exception')
		raise

@route('/test/start', method='PUT')
def testschotklokStart():

	ts.start()
	return "Started"

@route('/test/stop', method='PUT')
def testschotklokStop():

	ts.stop()
	return "Stopped"

@route('/test/reset', method='PUT')
def testschotklokReset():

	ts.reset()
	return "Stopped"

@route('/test/inError', method='PUT')
def testschotklokinError():

	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('inError'):
		abort(400, 'No inError specified')
	error = entity['inError']
	ts.inError(error)

@route('/test/time')
def testschotkloktime():

	return ts.getJSONTime()


s = schotklok.Schotklok()
ts = testschotklok.Testschotklok()

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config
logging.info('Started')
application = bottle.default_app()
