from database_io.utility.ServerResult import ServerResult
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import models
from home.models import Member

class ServerMemberIO:
	def __init__(self):
		self.memberManager = Member.objects
		
	def createMember(self,email,name,phone,address,biography,business,hasWebsite,hasMobileApp,hasTwitter):
		member = Member(email=email,name=name,phone=phone,address=address,biography=biography,business=business,has_Website=hasWebsite,has_Mobile_App=hasMobileApp,twitterAccount=hasTwitter)
		'''
		TODO
		Check for email in database before creation
		'''
		serverResult = ServerResult()
		try:
			member.full_clean()
			member.save()
			serverResult.model = member
		except ValidationError as v:
			serverResult.error.append(v)
		except IntegrityError as i:
			serverResult.error.append(i)
		return serverResult
		
	#def deleteMember(self,member):
		
	def displayMember(self,model):
		print("\nMember:")
		print("\tName: ",model.name)
		print("\tEmail: ",model.email)
		print("\tPhone: ",model.phone)
		print("\tAddress: ",model.address)
		print("\tBiography: ",model.biography)
		print("\tBusiness: ",model.business)
		print("\tHas a Website: ",model.has_Website)
		print("\tHas a Mobile App: ",model.has_Website)
		print("\tTwitter Account: ",model.twitterAccount)
		
	def getMemberByEmail(self,mail):
		serverResult = ServerResult()
		try:
			member = self.memberManager.get(email=mail)
			serverResult.model = member
		except ObjectDoesNotExist as o:
			serverResult.error.append(o)
		return serverResult
		
	def getMemberByName(self,name):
		serverResult = ServerResult()
		try:
			member = self.memberManager.get(name=name)
			serverResult.model = member
		except ObjectDoesNotExist as o:
			serverResult.error.append(o)
		return serverResult
		
	def updateMember(self,member):
		serverResult = ServerResult()
		try:
			member.full_clean()
			member.save()
			serverResult.model = member
		except ValidationError as v:
			serverResult.error.append(v)
		return serverResult
		
		