def onOffToOn(channel, sampleIndex, val, prev):
    activeBranchesList = op.GIT.ActiveRemoteBranches()
    op('branches/list_of_branches')[0,0] = activeBranchesList
	

