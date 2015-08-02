# Append current path to path.
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import scoreboard
import testscoreboard
import logging
import logging.config
import json


# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/score')
def scoreboardscore():

	try:
		logging.info('scoreboardpath() start')
		score = s.getJSONScore()
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
	ts.inError(error)


@route('/test/score', method='PUT')
def testscoreboardsetscore():

	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('home'):
		abort(400, 'No home specified')
	if not entity.has_key('away'):
		abort(400, 'No away specified')
	home = entity['home']
	away = entity['away']

	ts.setScore(home, away)

@route('/test/score')
def testscoreboardscore():

	return ts.getJSONScore()


s = scoreboard.Scoreboard()
ts = testscoreboard.Testscoreboard()

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config
logging.info('Started')
application = bottle.default_app()
