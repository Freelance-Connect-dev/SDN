from django.conf.urls import url
from . import views

###############################################################################
#   urlpatterns are the start of the chain fired off by django,
#   Use class_name.as_view() for class references from views.py, and use
#   views.method_name for method reference from views.py.
###############################################################################
urlpatterns = [
    # SDN.com/accounts/
    url(r'^$', views.AccountView.as_view(), name="account_page"),
    # SDN.com/accounts/register/
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    # SDN.com/accounts/login_user/
    url(r'^login_user/$',views.login_user,name='login_user'),
    # SDN.com/accounts/logout_user
    url(r'^logout_user/$',views.logout_user,name='logout_user'),
	# SDN.com/accounts/logout_user
    #url(r'^upload_file/$',views.UploadFile.as_view(),name='upload_file'),
	url(r'^upload_file/$',views.uploadfile,name='upload_file'),
]
