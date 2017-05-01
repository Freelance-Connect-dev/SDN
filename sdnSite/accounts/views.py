from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, File
from django.http import JsonResponse
from django.db.models import Q
from .forms import UserForm, FileUploadForm
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


# User account page
class AccountView(generic.DetailView):
    #TODO:find a way to load current logged in user (currently a non context page)
    model = User
    template_name = 'accounts/account.html'

    #user profile is loaded in account.html without context
    def get(self, request, profilename):
        #this is not working, need new field to query on
        print (profilename)
        profile = UserProfile.objects.get(user=profilename)
        return render(request, self.template_name, {'profile' : profile})




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

            # commit changes to the database
            user.save()


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

class UploadFile(generic.CreateView):
	model = File
	#put relevant fields to be displayed here
	#fields = ['picture']
    fields = ['title','file']

def uploadfile(request):
	img = UploadFileForm()
	if request.method=="POST":
		img = UploadFileForm(request.POST, request.FILES)
		if img.is_valid():
			img.save()
			return redirect('home:index')
		else:
			img = UploadFileForm()
	images=ProfilePicture.objects.all()
	return render(request,'accounts/profilepicture_form.html',{'form':img,'images':images})

class LoginView(View):

    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        # if form is complete and valid
        if form.is_valid():

            # take in cleaned data (protected)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # check that user doesnt already exist and name and pass are valid
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
                else:
                    return redirect('accounts/login.html')
            else:
                return redirect('accounts/login.html')

        return render(request, self.template_name, {'form':form})

class LogoutView(View):

    def get(self,request):
        logout(request)
        return redirect('home:index')




@login_required
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "account/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

# A dual use view, normal request gets login page, a POST request takes info and
#                   logs user in
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home/index.html')
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
