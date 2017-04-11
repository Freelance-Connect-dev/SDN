from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.PostingCreate.as_view(), name="create_posting"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^apply/$', views.application, name="application"),
    url(r'^congrats/$', views.congratulations, name="congrats"),
]
