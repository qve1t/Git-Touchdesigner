class Ext:
	"""
	Ext description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.toxPath = str(op('tox_folder_path')['tox','path'])

	def SaveAsTox(self, name, path):
		op(path).save("%s/%s.tox" % (self.toxPath, name))

	def AddExternalTox(self, path, currentToxName):
		op(path).par.externaltox = currentToxName
