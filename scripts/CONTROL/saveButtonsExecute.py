# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	if op.CONTROL.op('components_with_external_toxes')[channel.name, 'name'] != None:
		name = str(op.CONTROL.op('components_with_external_toxes')[channel.name, 'name'])
		path = str(op.CONTROL.op('components_with_external_toxes')[channel.name, 'path'])
		op.CONTROL.SaveAsTox(name, path)

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	