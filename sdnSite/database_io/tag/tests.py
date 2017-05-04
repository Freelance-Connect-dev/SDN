from django.test import TestCase
from home.models import Tag
from database_io.tag.ServerTagIO import ServerTagIO

class TagTestCase(TestCase):
	def setUp(self):
		self.stio = ServerTagIO()
		
	def testTagCreated(self):
		serverResult = self.stio.createTag("t0001","Java Programming","Proficiency in writing Java applications.")
		#Check if tag
		self.assertTrue(type(serverResult.model) is Tag)
		
	def testReadTagById(self):
		serverResult = self.stio.createTag("t0001","Java Programming","Proficiency in writing Java applications.")
		otherMember = self.stio.getTagById("t0001")
		self.assertTrue(type(otherMember.model) is Tag)
		
	def testDuplicateTag(self):
		firstTag = self.stio.createTag("t0001","Java Programming","Proficiency in writing Java applications.")
		secondTag = self.stio.createTag("t0001","Python Programming","Proficiency in writing Python scripts.")
		#Check if serverResult has errors
		self.assertTrue(secondTag.hasErrors())
		
	def testNameTooShort(self):
		serverResult = self.stio.createTag("t0001","IO","Input/Output.")
		self.assertTrue(serverResult.hasErrors())