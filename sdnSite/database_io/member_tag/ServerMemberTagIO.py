from database_io.utility.ServerResult import ServerResult
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import models
from home.models import Member_Tag

class ServerMemberTagIO:
	def __init__(self):
		self.memberTagManager = Member_Tag.objects
		
	def createMemberTag(self,member,tag):
		memberTag = Member_Tag(member_id=member,skill_id=tag)
		serverResult = ServerResult()
		
		try:
			memberTag.full_clean()
			memberTag.save()
			serverResult.model = memberTag
		except ValidationError as v:
			serverResult.error.append(v)
		except IntegrityError as i:
			serverResult.error.append(i)
		return serverResult
		
	def displayTag(self,model):
		print("\nTag ID: ",model.skill_id.skill_id)
		print("Member ID: ",model.member_id.email)