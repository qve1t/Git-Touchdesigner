def onOffToOn(channel, sampleIndex, val, prev):
	commandToRun = op.GIT.gitCommands['checkout', 'command']
    op.GIT.RunCommand(commandToRun, channel.name)
    #przetestować jak github znowu zacznie dzialac