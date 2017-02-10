from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('This is the login page')

def newemployer(request):
    return HttpResponse('This is the creation page for new Contractors')

def newworker(request):
    return HttpResponse('This is the creation page for new workers')
