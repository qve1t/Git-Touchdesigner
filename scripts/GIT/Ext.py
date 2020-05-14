import subprocess

class Ext:
	"""
	Ext description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.cmdOutput = op('cmd_output')

	def RunCommand(self, command):
		#command should be a list of strings
		process = subprocess.Popen(command, stdout=subprocess.PIPE)
		return process.communicate()[0]

	def PrintOutput(self, message):
		self.cmdOutput.text = message.decode() 

	def CommandGitStatus(self):
		command = ["git", 'status']
		self.PrintOutput(self.RunCommand(command))