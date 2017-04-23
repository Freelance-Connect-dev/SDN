from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models.signals import post_save


# Override of Django's user class to accomodate our needs can go here
# TODO: read up on django's built in methods that we can use to reduce work
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)
	
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)
	
class File(models.Model):
	file_id = models.AutoField(primary_key=True);
	#business_id = models.ForeignKey(Member,on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	#file_reference = models.CharField(max_length=100) #Assuming a web link
	file = models.FileField(null=True)
