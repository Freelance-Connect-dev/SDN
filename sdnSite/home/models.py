from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
	email = models.EmailField(primary_key=True)
	name = models.CharField(max_length=50)
	phone = models.IntegerField()
	address = models.CharField(max_length=50)
	biography = models.CharField(max_length=300)
	business = models.BooleanField(default=False)
	#Account links could become its own table to
	#ensure that the data entered remains atomic.

class Posting(models.Model):
	job_id = models.IntegerField(primary_key=True);
	employer_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	job_title = models.CharField(default="make an app", max_length=50)
	description = models.CharField(default="a decent job", max_length=1000)
	#status could be set up as a list of choices
	status = models.IntegerField(default=0)
	finish_date = models.DateTimeField(default=timezone.now)
	post_date = models.DateTimeField(default=timezone.now)

class Image(models.Model):
	image_id = models.IntegerField(primary_key=True)
	member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	#image_reference = models.ImageField() #lets just fill this attribute with image links
	title = models.CharField(max_length=30)

class File(models.Model):
	file_id = models.IntegerField(primary_key=True);
	business_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	file_reference = models.CharField(max_length=100) #Assuming a web link

class Tag(models.Model):
	skill_id = models.IntegerField(max_length=30,primary_key=True)
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

class Contract(models.Model):
	contract_id = models.IntegerField(primary_key=True)
	job_id = models.ForeignKey(Posting,on_delete=models.CASCADE)
	contractor_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	deliverable = models.CharField(max_length=1000)
	total_pay = models.FloatField()
	percent_up_front = models.FloatField()
	create_date = models.DateTimeField(default=timezone.now)

class Application(models.Model):
	app_id = models.IntegerField(primary_key=True)
	job_id = models.ForeignKey(Posting)
	member_id = models.ForeignKey(Member)
	create_date = models.DateTimeField(default=timezone.now)
	cover_letter = models.CharField(max_length=1000)
	resume_id = models.ForeignKey(File)
