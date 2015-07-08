import subprocess
from datetime import datetime

class Command:

	@staticmethod
	def _run(cmd):
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		out = p.communicate()

		return out

	@staticmethod		
	def usestub(value):

		if value:
			out = Command._run(['use-stub.sh','on'])
		else:
			out = Command._run(['use-stub.sh','off'])
		return out

	@staticmethod
	def createsupportbundle():

		filename = 'support-' + datetime.strftime(datetime.now(), '%Y%m%d-%H%M%S') + '.zip'
		out = Command._run(['zip','-r',filename,'/var/log/apache2/','/var/log/digits/'])
		return filename
