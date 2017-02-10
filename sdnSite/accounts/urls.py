from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'login', views.login),
    url(r'new_employer', views.newemployer),
    url(r'new_worker', views.newworker),
]
