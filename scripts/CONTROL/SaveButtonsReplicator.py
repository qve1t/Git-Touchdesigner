def onRemoveReplicant(comp, replicant):

	replicant.destroy()
	return

def onReplicate(comp, allOps, newOps, template, master):

	for c in newOps:

		c.par.display = 1
		c.par.enable = 1
		c.name = op('externals_to_save')[c.digits, 0]
		c.outputConnectors[0].connect(op('save_buttons_signals'))


	return
