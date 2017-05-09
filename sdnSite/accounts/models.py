from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Override of Django's user class to accomodate our needs can go here
# TODO: read up on django's built in methods that we can use to reduce work
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    state = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)
    resume = models.FileField(upload_to="resumes",default="resumes/hello.txt")
    picture = models.ImageField(upload_to="profile_pictures",default="profile_pictures/Happy_Toby.jpg")

    @receiver(post_save,sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)



class ProfilePicture(models.Model):
	picture = models.ImageField(upload_to="profile_pictures")
