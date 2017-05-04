from django.test import TestCase
from home.models import Member_Tag
from database_io.member.ServerMemberIO import ServerMemberIO
from database_io.member_tag.ServerMemberTagIO import ServerMemberTagIO
from database_io.tag.ServerTagIO import ServerTagIO

class TagTestCase(TestCase):
	def setUp(self):
		self.smio = ServerMemberIO()
		self.smtio = ServerMemberTagIO()
		self.stio = ServerTagIO()
		
	def testMemberTagCreated(self):
		firstMember = self.smio.createMember("freelance@fakemail.com","Freelance", 5673949888,"Fake Boulevard","We are in school.",True,False,False,"@freelance")
		firstTag = self.stio.createTag("t0001","Java Programming","Proficiency in writing Java applications.")
		serverResult = self.smtio.createMemberTag(firstMember.model,firstTag.model)
		#Check if member tag
		self.smtio.displayTag(serverResult.model)
		self.assertTrue(type(serverResult.model) is Member_Tag)
