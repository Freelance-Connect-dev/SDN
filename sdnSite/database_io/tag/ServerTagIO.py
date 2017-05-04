from database_io.utility.ServerResult import ServerResult
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import models
from home.models import Tag

class ServerTagIO:
	def __init__(self):
		self.tagManager = Tag.objects
		
	def createTag(self,skill_id,skill_name,description):
		tag = Tag(skill_id=skill_id,skill_name=skill_name,description=description)
		serverResult = ServerResult()
		#Special checks before creating tags
		if(len(skill_name) < 3):
			serverResult.error.append("Skill name")
			return serverResult
		
		
		try:
			tag.full_clean()
			tag.save()
			serverResult.model = tag
		except ValidationError as v:
			serverResult.error.append(v)
		except IntegrityError as i:
			serverResult.error.append(i)
		return serverResult
		
	def displayTag(self,model):
		print("\nTag ID: ",model.skill_id)
		print("\tName: ",model.skill_name)
		print("\tDescription: ",model.description)
		
	def getTagById(self,id):
		serverResult = ServerResult()
		try:
			tag = self.tagManager.get(skill_id=id)
			serverResult.model = tag
		except ObjectDoesNotExist as o:
			serverResult.error.append(o)
		return serverResult