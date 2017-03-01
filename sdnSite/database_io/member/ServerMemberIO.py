from django.core.exceptions import ValidationError
from django.db import models
from home.models import Member

class ServerMemberIO:
	def __init__(self):
		self.memberManager = Member.objects
		
	def createMember(self,email,name,phone,address,biography):
		member = Member(email=email,name=name,phone=phone,address=address,biography=biography)
		try:
			member.full_clean()
			member.save()
		except ValidationError as v:
			return v
		except IntegrityError as i:
			return i
		return member
		
	#def deleteMember(self,member):
		
	def displayMember(self,model):
		print("\nMember:")
		print("\tName: ",model.name)
		print("\tEmail: ",model.email)
		print("\tPhone: ",model.phone)
		print("\tAddress: ",model.address)
		print("\tBiography: ",model.biography)
		
	def getMemberByEmail(self,mail):
		member = self.memberManager.get(email=mail)
		return member
		
	def getMemberByName(self,name):
		member = self.memberManager.get(name=name)
		return member
		
	def updateMember(self,member):
		try:
			member.full_clean()
			member.save()
		except ValidationError as v:
			return v
		
		
		