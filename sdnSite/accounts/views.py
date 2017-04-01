from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from .forms import UserForm
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


# User account page
class AccountView(generic.DetailView):
    #find a way to load current logged in user (currently a non context page)
    template_name = 'accounts/account.html'

# User creation
class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/registration_form.html'

    # display blank form for new user to fill out
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # process form data when user submits
    def post(self, request):
        form = self.form_class(request.POST)

        # if form is complete and valid
        if form.is_valid():
            # save form data without changing database
            user = form.save(commit=False)

            # take in cleaned data (protected)
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # set the pass word safely
            user.set_password(password)

            # commit changes to the database, not sure why this is done before
            # authenticating
            user.save()

            # check that user doesnt already exist and name and pass are valid
            user = authenticate(username=username, password=password)

            # for security, check that user is still valid
            if user is not None:

                # check that this user is active before logging in and sending away
                if user.is_active:
                    # login in and create session id
                    login(request, user)
                    # send to home
                    return redirect('home:index')

        # if this is where user ended up, their form wasnt valid.
        # so send them back with a message about what was wrong.
        return render(request, self.template_name, {'form':form})


# Create your method views here. -- these should be reconfigured to class views

# A dual use view, normal request gets login page, a POST request takes info and
#                   logs user in
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/index.html')
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')

# This is a route to the login page, logging the user out upon arrival
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form" : form,
    }
    return render(request, 'accounts/login.html', context)
