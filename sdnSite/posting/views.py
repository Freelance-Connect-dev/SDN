from django.shortcuts import render, HttpResponse

# Create your views here.
def forhire(request):
    return render(request, 'posting/workforhire.html')

def job(request):
    return render(request, 'posting/job.html')

def employment(request):
    return render(request, 'posting/employment.html')
