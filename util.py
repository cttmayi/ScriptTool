import subprocess


class util():
	@staticmethod
	def runWait(cmd):
		subprocess.call(cmd.split(' '), shell=True)
	@staticmethod
	def runWaitOutputString(cmd):
		return subprocess.check_output(cmd.split(' '), shell=True)
	
	@staticmethod
	def runNoWaitOutputPipe(cmd):
		return subprocess.Popen(cmd.split(' '), shell=True,stdout=subprocess.PIPE).stdout
		
		
				