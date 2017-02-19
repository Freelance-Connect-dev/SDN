from django.db import models

# Create your models here.
class Posting(models.Model):
	job_id = models.IntegerField();
	contractor_id = models.CharField(max_length=30)
	employer_id = models.CharField(max_length=30)
	job_title = models.CharField(max_length=30)
	description = models.CharField(max_length=500)
	finish_date = models.DateTimeField()
	post_date = models.DateTimeField()
	pay_amount = models.FloatField()

class Member(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=50)
	phone = models.IntegerField()
	address = models.CharField(max_length=50)
	biography = models.CharField(max_length=300)
	#Account links could become its own table to
	#ensure that the data entered remains atomic.
	
class Image(models.Model):
	image_id = models.CharField(max_length=30)
	business_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	image_reference = models.ImageField()
	title = models.CharField(max_length=30)
	profile_picture = models.BooleanField(default=False);
	
class File(models.Model):
	file_id = models.IntegerField();
	business_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	file_reference = models.CharField(max_length=100) #Assuming a web link