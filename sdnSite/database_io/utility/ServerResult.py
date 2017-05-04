from django.db import models

class ServerResult:
	def __init__(self):
		self.model = None
		self.error = []
		self.serverCode = None
		
	def hasErrors(self):
		return (len(self.error) > 0)
		
	def hasModel(self):
		if(type(self.model) is models):
			return True
		else:
			return False
			
