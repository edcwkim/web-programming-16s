from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import resolve_url
from django.views import generic


class Register(generic.CreateView):

    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        nxt = ""
        if self.request.GET.get("next", ""):
            nxt = "?next={}".format(self.request.GET['next'])
        return resolve_url(settings.LOGIN_URL + nxt)
