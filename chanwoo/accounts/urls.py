from django.conf.urls import url
from django.contrib.auth import views as django_views
from . import views

urlpatterns = [
    url(r'^login/$', django_views.login, name='login'),
    url(r'^logout/$', django_views.logout, name='logout'),
    url(r'^register/$', views.Register.as_view(), name='register'),
]
