from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, ProfilePicture

###############################################################################
# Forms in django are meant for building, displaying, and accepting info on models
# from models.py. Build form with relevant info based on model, then give the form
# to the form template inside the html page. This is how Django takes care of things
###############################################################################

class UserForm(forms.ModelForm):
    # passwords get protected
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: # data to be grabbed in forms (relevant fields from models)
        model = User
        fields = ['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['website','bio','phone','city','state','country','organization']
        exclude = ['resume','picture']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UploadResumeForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['resume']
		exclude = ['user','website','bio','phone','city','country','organization','picture']
		
class UploadPictureForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['picture']
		exclude = ['user','website','bio','phone','city','country','organization','resume']

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = ProfilePicture
        fields = ['picture']
