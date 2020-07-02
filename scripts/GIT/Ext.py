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
		self.username = op('GUI/account_panel/data_container/username_null')[0,0]
		self.password = op('GUI/account_panel/data_container/password_null')[0,0]
		self.commandsToCheck = ['fetch', 'pull', 'push']

	def getRepoUrl(self):
		commandToRun = self.GitCommands['getUrl', 'command']
		repoFullUrl = self.RunCommand(command=commandToRun).decode().replace("https://", "").replace("\n", "")
		return repoFullUrl

	def GitUsernameAndPassword(self):
		if "bitbucket" in self.getRepoUrl():
			return "https://%s" % (self.getRepoUrl())

		return "https://%s:%s@%s" % (str(self.username), str(self.password), self.getRepoUrl())

	def OutputClean(self):
		self.cmdOutput.text = ""

	def PrintOutput(self, message):
		self.cmdOutput.text = self.MessageDecode(message)

	def MessageDecode(self, message):
		try:
			return message.decode()
		except:
			return message 
			
	def RunCommand(self, command, customMessage=None, usePass=False):
		#command should be a list of strings
		commandList = str(command).split(" ")
		if self.gitCommandReplace in commandList:
			if customMessage == None:
				commandList[commandList.index("MESSAGE")] = str(op('message')[0,0])
			else:
				commandList[commandList.index("MESSAGE")] = customMessage

		#add username and password to repo
		if usePass:
			commandList.append(self.GitUsernameAndPassword())

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

		usePassword = False
		if command in self.commandsToCheck:
			usePassword = True

		self.PrintOutput(self.RunCommand(command=commandToRun, usePass=usePassword))

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
