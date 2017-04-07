from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /home/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
]
