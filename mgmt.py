import subprocess, os
from datetime import datetime
import logging

path = os.path.dirname(__file__) + '/scripts/'

class Command:

	@staticmethod
	def _run(cmd):
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		out = p.communicate()

		return str(out)

	@staticmethod		
	def stub():

		out = Command._run(['ls','-l',path + '../IOPi'])
		return out

	@staticmethod		
	def usestub(value):

		if value:
			out = Command._run([path + 'use-stub.sh','on'])
		else:
			out = Command._run([path + 'use-stub.sh','off'])
		return out

	@staticmethod
	def createsupportbundle():

		filename = 'support-' + datetime.strftime(datetime.now(), '%Y%m%d-%H%M%S') + '.zip'
		out = Command._run(['zip','-r',filename,'/var/log/apache2/','/var/log/digits/'])
		return filename

	@staticmethod
	def reboot():

		out = Command._run(['sudo','reboot'])
		return out

	@staticmethod
	def poweroff():

		out = Command._run(['sudo','poweroff'])
		return out
	@staticmethod
	def update():

		out = Command._run(['sudo','su','-','-c',path + 'update.sh'])
		return out
