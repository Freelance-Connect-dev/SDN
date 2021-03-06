from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

###############################################################################
#   urlpatterns are the start of the chain fired off by django,
#   Use class_name.as_view() for class references from views.py, and use
#   views.method_name for method reference from views.py.
###############################################################################
urlpatterns = [
    # SDN.com/accounts/register/
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    # SDN.com/accounts/login_user/
    url(r'^login_user/$',views.LoginView.as_view(),name='login_user'),
    # SDN.com/accounts/logout_user
    url(r'^logout_user/$',views.LogoutView.as_view(),name='logout_user'),
	url(r'^upload_picture/$',views.uploadPicture,name='upload_picture'),
	url(r'^upload_resume/$',views.uploadResume,name='upload_resume'),
	# SDN.com/accounts/ ^(?P<profilename>)
    url(r'^$', views.AccountView.as_view(), name="account_page"),
]
