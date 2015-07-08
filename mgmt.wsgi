# Append current path to path.
import sys, os

sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import logging
import logging.config
import json
import mgmt

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/createsupportbundle', method='PUT')
def createsupportbundle():

	try:
		logging.debug('createsupportbundle() start')
		out = mgmt.Command.createsupportbundle()
		logging.debug('createsupportbundle() end')
		return out
	except:
		logging.exception('Uncaught exception')
		raise

@route('/stub', method='GET')
def getstub():

	logging.debug('getstub() start')

        result = mgmt.Command.stub()

	logging.debug('getstub() stop')
        return result

@route('/stub', method='PUT')
def usestub():

	logging.debug('putstub() start')

        data = request.body.readline()
        if not data:
                abort(400, 'No data received')
        entity = json.loads(data)
        if not entity.has_key('stub'):
                abort(400, 'No stub specified')
        stub = entity['stub']

        result = mgmt.Command.usestub(stub == 'True')

	logging.debug('putstub() stop')
        return result

@route('/reboot', method='PUT')
def reboot():

	logging.info('Rebooting')

	return mgmt.Command.reboot()

@route('/poweroff', method='PUT')
def poweroff():

	logging.info('Poweroff')

	return mgmt.Command.poweroff()

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config
logging.info('Started')
application = bottle.default_app()
