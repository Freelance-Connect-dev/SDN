from django.contrib import admin

# Register your models here.
from .models import UserProfile, ProfilePicture

admin.site.register(UserProfile)
admin.site.register(ProfilePicture)
