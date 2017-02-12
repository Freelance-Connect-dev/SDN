from django.shortcuts import render, HttpResponse, render
from django.template import loader
from django.http import Http404

from .models import Posting

# Create your views here.
def index(request):
    latest_posting_list = Posting.objects.order_by('-pub_date')[:5]
    context = {'latest_posting_list': latest_posting_list}
    return render(request, 'home/index.html', context)


def worker(request):
    return render(request, 'home/worker.html')

def employer(request):
    return render(request, 'home/employer.html')
