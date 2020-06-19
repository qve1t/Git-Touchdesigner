
def onOffToOn(channel, sampleIndex, val, prev):
	if op.CONTROL.op('components_without_external_toxes')[channel.name, 'name'] != None:
		name = str(op.CONTROL.op('components_without_external_toxes')[channel.name, 'name'])
		path = str(op.CONTROL.op('components_without_external_toxes')[channel.name, 'path'])
		op.CONTROL.SaveAsTox(name, path)

	toxPath ='tox/'+channel.name+'.tox'
	addExternal ="op.CONTROL.AddExternalTox('%s', '%s')" % (path, toxPath)
	
	run(addExternal, delayFrames=10)