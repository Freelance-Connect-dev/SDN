from django.shortcuts import render, HttpResponse, render
from django.template import loader
from django.http import Http404
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.db import models
from posting.models import posting


class IndexView(TemplateView):

    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_posting_list'] = posting.objects.all()
        return context

# Create your views here.
def index(request):
    latest_posting_list = posting.objects.order_by('-pub_date')
    context = {'latest_posting_list': latest_posting_list}
    return render(request, 'home/index.html', context)


def worker(request):
    return render(request, 'home/worker.html')

def employer(request):
    return render(request, 'home/employer.html')
