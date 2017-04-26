from django import forms
from .models import posting
from django.contrib.admin.widgets import AdminDateWidget

###############################################################################
# Forms in django are meant for building, displaying, and accepting info on models
# from models.py. Build form with relevant info based on model, then give the form
# to the form template inside the html page. This is how Django takes care of things
###############################################################################

class PostingForm(forms.ModelForm):

    class Meta:
        model = posting
        exclude = ['post_id','post_date', 'status']
    # 
    # def __init__ (self, *args, **kwargs):
    #     self.fields["tags"].widget = forms.widgets.CheckboxSelectMultiple()
