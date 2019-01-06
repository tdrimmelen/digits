# Append current path to path.
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import testscoreboard
import testtimeclock
import logging
import logging.config
import json
import importlib
import ConfigParser 

configFileName = os.path.dirname(__file__) + '/digits.cfg'


# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/score')
def scoreboardscore():

	try:
		logging.info('scoreboardpath() start')
		score = sb.getJSONScore()
		logging.info('scoreboardpath() end')
		return score
	except:
		logging.exception('Uncaught exception')
		raise

@route('/test/inError', method='PUT')
def testtimeclockinError():
	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('inError'):
		abort(400, 'No inError specified')
	error = entity['inError']
	tsb.inError(error)
	ttc.inError(error)


@route('/test/score', method='PUT')
def testscoreboardsetscore():

	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('home'):
		abort(400, 'No home specified')
	if not entity.has_key('guest'):
		abort(400, 'No guest specified')
	home = entity['home']
	guest = entity['guest']

	tsb.setScore(home, guest)

@route('/test/score')
def testscoreboardscore():

	return tsb.getJSONScore()

@route('/time')
def timeclocktime():

	try:
		logging.info('timeclockpath() start')
		time = tc.getJSONTime()
		logging.info('timeclockpath() end')
		return time
	except:
		logging.exception('Uncaught exception')
		raise

@route('/test/start', method='PUT')
def testtimeclockStart():

	ttc.start()
	return "Started"

@route('/test/stop', method='PUT')
def testtimeclockStop():

	ttc.stop()
	return "Stopped"

@route('/test/reset', method='PUT')
def testtimeclockReset():

	ttc.reset()
	return "Reset executed"

@route('/test/startstop', method='PUT')
def testtimeclockStartStop():

	ttc.startstop()
	if ttc.getRunning():
		return "Started"
	else:
		return "Stopped"

@route('/test/time')
def testtimeclocktime():

	return ttc.getJSONTime()

@route('/test/time', method='PUT')
def testscoreboardsetscore():

	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('minute'):
		abort(400, 'No minue specified')
	if not entity.has_key('second'):
		abort(400, 'No second specified')
	minute = entity['minute']
	second = entity['second']

	ttc.setTime(minute, second)

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config


#Read shotclock from config file
config = ConfigParser.RawConfigParser()
config.read(configFileName)
type = config.get('Scoreboard', 'type')

# Start the configured scoreboard class
module = importlib.import_module(type)
class_ = getattr(module, type.capitalize())

sb = class_(configFileName)

type = config.get('Timeclock', 'type')

if (type != ""):
	# Start the configured timeclock class
	module = importlib.import_module(type)
	class_ = getattr(module, type.capitalize())

	tc = class_(configFileName)

tsb = testscoreboard.Testscoreboard()
ttc = testtimeclock.Testtimeclock()

logging.info('Started')
application = bottle.default_app()
