from django.shortcuts import render, HttpResponse
from .forms import PostingForm
from django.views import generic
from django.views.generic import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import posting

# Create Posting page
class PostingCreate(generic.CreateView):
    model = posting
    #put relevant fields to be displayed here
    fields = ['post_id','post_title','description', 'finish_date']

class DetailView(DetailView):
    model = posting
    template_name = 'posting/detail.html'




# Create your views here.
def forhire(request):
    return render(request, 'posting/workforhire.html')

def job(request):
    return render(request, 'posting/job.html')

def employment(request):
    return render(request, 'posting/employment.html')
