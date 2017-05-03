from django import forms
from .models import posting
from django.forms.extras import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _
###############################################################################
# Forms in django are meant for building, displaying, and accepting info on models
# from models.py. Build form with relevant info based on model, then give the form
# to the form template inside the html page. This is how Django takes care of things
###############################################################################

class PostingForm(forms.ModelForm):

    class Meta:
        model = posting
        exclude = ['post_id','post_date', 'status']
        #description = forms.CharField( widget=forms.TextArea)
        #finish_date = forms.DateField(widget=forms.SelectDateWidget())
        widgets = {
            'finish_date': SelectDateWidget(attrs={'style': 'width:10.5%'}),
            'description': forms.Textarea(attrs={'placeholder': 'Job Description', 'cols': 50, 'rows': 10}),
            'post_title': forms.Textarea(attrs={'cols': 50, 'rows': 1}),
            'company_name': forms.Textarea(attrs={'cols': 50, 'rows': 1}),
            'total_pay': forms.NumberInput(attrs={'step': 100, 'style': 'width:50ch'}),
            #'percent_up_front': forms.NumberInput(attrs={'step': 5, 'style': 'width:50ch'}),
            'tags': forms.SelectMultiple(attrs={'style': 'width:50ch'})
            #'tags': CheckboxSelectMultiple()
        }
        labels = {
            "description": _("Job Description")
        }
        help_texts = {
            'description': _("geeeererrrerr")
        }
