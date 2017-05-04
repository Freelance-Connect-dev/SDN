from django.shortcuts import render, HttpResponse
from .forms import PostingForm
from django.views import generic
from django.views.generic import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import posting
from django.contrib.admin.widgets import AdminDateWidget
# Create Posting page
# class PostingCreate(generic.CreateView):
#     model = posting
#     #put relevant fields to be displayed here
#     fields = ['post_id','post_title', 'company_name', 'description', 'total_pay', 'finish_date', 'tags']
#     class Meta:
#         widgets = {
#             'finish_date': AdminDateWidget()
#         }



class DetailView(DetailView):
    model = posting
    template_name = 'posting/detail.html'

def new_post(request):
    if request.method == "POST":
        form = PostingForm(request.POST)
    else:
        form = PostingForm()
    if form.is_valid():
        posting = form.save(commit=False)
        posting.save()

    return render(request, 'posting/posting_form.html', {'form':form})

def application(request):
    return render(request, 'posting/application.html')

def congratulations(request):
    return render(request, 'posting/congratulations.html')
