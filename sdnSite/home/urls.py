from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /home/
    url(r'^$', views.index, name='index'),
    # ex: /home/worker/
    url(r'^worker/$', views.worker, name='worker'),
    # ex: /home/employer/
    url(r'^employer/$', views.employer, name='employer'),
]
