class Ext:
	"""
	Ext description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.toxPath = str(op('tox_folder_path')['tox','path'])

	def SaveAsTox(self, name, path):
		op(path).save(self.toxPath + '/' + name + '.tox')