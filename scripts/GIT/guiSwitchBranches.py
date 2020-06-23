def onOffToOn(channel, sampleIndex, val, prev):
    commandToRun = op.GIT.GitCommands['checkout', 'command']
    op.GIT.PrintOutput(op.GIT.RunCommand(commandToRun, channel.name))
    #przetestować jak github znowu zacznie dzialac