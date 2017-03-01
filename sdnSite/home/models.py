from django.db import models
from django.utils import timezone

# Create your models here.
class Posting(models.Model):

	job_id = models.IntegerField(default=0);
	contractor_id = models.CharField(default=0, max_length=30)
	employer_id = models.CharField(default=1, max_length=30)
	job_title = models.CharField(default="make an app", max_length=30)
	description = models.CharField(default="a decent job", max_length=500)
	#status could be set up as a list of choices
	finish_date = models.DateTimeField(default=timezone.now)
	post_date = models.DateTimeField(default=timezone.now)
	pay_amount = models.FloatField(default=1000.95)

class Member(models.Model):
	email = models.EmailField(primary_key=True)
	name = models.CharField(max_length=50,unique=True)
	phone = models.IntegerField()
	address = models.CharField(max_length=50)
	biography = models.CharField(max_length=300)
	#Account links could become its own table to
	#ensure that the data entered remains atomic.

class Image(models.Model):
	image_id = models.CharField(max_length=30)
	member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	#image_reference = models.ImageField() #lets just fill this attribute with image links
	title = models.CharField(max_length=30)
	profile_picture = models.BooleanField(default=False);

class File(models.Model):
	file_id = models.IntegerField();
	business_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	file_reference = models.CharField(max_length=100) #Assuming a web link

class Tag(models.Model):
	skill_id = models.CharField(max_length=30,primary_key=True)
	skill_name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)

class Job_Tag(models.Model):
	job_id = models.ForeignKey(Posting,on_delete=models.CASCADE)
	skill_id = models.ForeignKey(Tag,on_delete=models.CASCADE)

class Member_Tag(models.Model):
	member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	skill_id = models.ForeignKey(Tag,on_delete=models.CASCADE)

class Review(models.Model):
	job_id = models.ForeignKey(Posting,on_delete=models.CASCADE)
	reviewer_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	#reviewee_id = models.ForeignKey(Member,on_delete=models.CASCADE)
