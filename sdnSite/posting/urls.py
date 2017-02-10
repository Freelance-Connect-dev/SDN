from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'for_hire', views.forhire),
    url(r'job', views.job),
    url(r'employment', views.employment),
]
