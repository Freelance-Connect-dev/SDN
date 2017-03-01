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
		member = self.smio.createMember("freelance@fakemail.com","Freelance", 5673949888,"Fake Boulevard","We are in school.")
		#Check if member
		self.assertTrue(type(member) is Member)
		
	def testDuplicateEmail(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.")
		otherMember = self.smio.createMember("lance@fakemail.com","Other Lance", 5673949888,"Fake Boulevard","We are in school.")
		#Check if other member added
		self.assertFalse(type(otherMember) is Member)
		
	def testDuplicateName(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.")
		otherMember = self.smio.createMember("free@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.")
		#Check if other member added
		self.assertFalse(type(otherMember) is Member)
		
	def testReadMemberByEmail(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.")
		otherMember = self.smio.getMemberByEmail("lance@fakemail.com")
		self.assertTrue(type(otherMember) is Member)
		
	def testReadMemberByName(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.")
		otherMember = self.smio.getMemberByName("Lance")
		self.assertTrue(type(otherMember) is Member)	
	'''
	def testUpdateMember(self):
		member = self.smio.createMember("lance@fakemail.com","Lance", 5673949888,"Fake Boulevard","We are in school.")
		member.name = "New Lance"
		self.smio.updateMember(member)
		
		otherMember = self.smio.getMemberByName("New Lance")
		otherMember.address = "HEge"
		self.assertTrue(otherMember == member)	
	'''
		
		