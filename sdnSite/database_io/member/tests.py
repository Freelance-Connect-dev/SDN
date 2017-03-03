from django.core.exceptions import ValidationError
from django.test import TestCase
from home.models import Member
from database_io.member.ServerMemberIO import ServerMemberIO

# Create your tests here.
class MemberTestCase(TestCase):
	def setUp(self):
		self.smio = ServerMemberIO()
		
	def testMemberCreated(self):
		#Create member.  Will return validation error if fields incorrect
		serverResult = self.smio.createMember("freelance@fakemail.com","Freelance", 5673949888,"Fake Boulevard","We are in school.",True)
		#Check if member
		self.assertTrue(type(serverResult.model) is Member)
		
	def testReadMemberByEmail(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		otherMember = self.smio.getMemberByEmail("lance@fakemail.com")
		self.assertTrue(type(otherMember.model) is Member)
		
	def testReadMemberByName(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		otherMember = self.smio.getMemberByName("Lance")
		self.assertTrue(type(otherMember.model) is Member)
		
	def testDuplicateEmail(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		otherMember = self.smio.createMember("lance@fakemail.com","Other Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		#Check if serverResult has errors
		self.assertTrue(otherMember.hasErrors())
		
	def testDuplicateName(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		otherMember = self.smio.createMember("free@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		#Check if other member added
		self.assertTrue(otherMember.hasErrors())
		
	def testUpdateMember(self):
		serverResult = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.",True)
		member = serverResult.model
		member.name = "New Lance"
		self.smio.updateMember(member)
		otherMember = self.smio.getMemberByName("New Lance")
		self.assertTrue(otherMember.model.email == "lance@fakemail.com")

		
		