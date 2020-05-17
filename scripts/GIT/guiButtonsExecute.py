
def onOffToOn(channel, sampleIndex, val, prev):
	if channel.name == "clean":
		op.GIT.OutputClean()
	else:
		if channel.name == "commit" and op('message_null')[0,0] == "":
			op.GIT.PrintOutput("Write commit message")
			return

		op.GIT.RunGitCommand(channel.name)

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	