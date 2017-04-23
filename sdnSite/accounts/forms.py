from django import forms
from django.contrib.auth.models import User
from .models import File

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
		
class FileUploadForm(forms.ModelForm):

	class Meta:
		model = File
		fields = ['title','file']
