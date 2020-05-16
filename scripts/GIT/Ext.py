import subprocess

class Ext:
	"""
	Ext description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.gitCommandReplace = "MESSAGE"
		self.cmdOutput = op('cmd_output')
		self.gitCommands = op('git_commands')

	def RunCommand(self, command):
		#command should be a list of strings
		commandList = str(command).split(" ")
		if self.gitCommandReplace in commandList:
			commandList[commandList.index("MESSAGE")] = str(op('message')[0,0])

		process = subprocess.Popen(commandList, stdout=subprocess.PIPE)
		
		return process.communicate()[0]

	def PrintOutput(self, message):
		self.cmdOutput.text = self.MessageDecode(message)

	def MessageDecode(self, message):
		try:
			return message.decode()
		except:
			return message 

	def RunGitCommand(self, command):
		commandToRun = self.gitCommands[command, 'command']
		if commandToRun == None:
			self.PrintOutput("Wrong command")
			return

		self.PrintOutput(self.RunCommand(commandToRun))