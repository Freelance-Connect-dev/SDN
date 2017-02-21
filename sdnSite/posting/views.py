from django.shortcuts import render, HttpResponse

# Create your views here.
def forhire(request):
    return HttpResponse('This is where workers can post themselves for employment or work')

def job(request):
    return HttpResponse('This is where Conctractors or Workers can post a job that needs to be done')

def employment(request):
    return HttpResponse('This is where Contractors can post short term/long term employment opportunities')
