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
		self.GitCommands = op('git_commands')

	def OutputClean(self):
		self.cmdOutput.text = ""

	def PrintOutput(self, message):
		self.cmdOutput.text = self.MessageDecode(message)

	def MessageDecode(self, message):
		try:
			return message.decode()
		except:
			return message 
			
	def RunCommand(self, command, customMessage=None):
		#command should be a list of strings
		commandList = str(command).split(" ")
		if self.gitCommandReplace in commandList:
			if customMessage == None:
				commandList[commandList.index("MESSAGE")] = str(op('message')[0,0])
			else:
				commandList[commandList.index("MESSAGE")] = customMessage

		process = subprocess.Popen(commandList, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

		#return success
		if process.communicate()[0]:
			return process.communicate()[0]

		#return error	
		return process.communicate()[1]

	def RunGitCommand(self, command):
		commandToRun = self.GitCommands[command, 'command']
		if commandToRun == None:
			self.PrintOutput("Wrong command")
			return

		self.PrintOutput(self.RunCommand(commandToRun))

	def ActiveRemoteBranches(self):
		commandToRun = self.GitCommands['branches', 'command']
		text = self.RunCommand(commandToRun).decode()
		if text == '':
			return []

		#last element is an empty string
		activeBranches = text.split('\n')[:-1]
		for index,elem in enumerate(activeBranches):
			#take names of active branches
			activeBranches[index] = elem.split('heads/')[1]
		
		return activeBranches