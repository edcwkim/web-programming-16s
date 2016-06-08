from django.conf.urls import url
from django.contrib.auth import views as django_views

urlpatterns = [
    url(r'^login/$', django_views.login, name='login'),
    url(r'^logout/$', django_views.logout, name='logout'),
]
