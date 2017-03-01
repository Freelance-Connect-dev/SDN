from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def newemployer(request):
    return render(request, 'accounts/new_employer.html')

def newworker(request):
    return render(request, 'accounts/new_worker.html')
