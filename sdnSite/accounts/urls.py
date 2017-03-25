from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.AccountView.as_view(), name="account_page"),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^login_user/$',views.login_user,name='login_user'),
    url(r'^logout_user/$',views.logout_user,name='logout_user'),
]
