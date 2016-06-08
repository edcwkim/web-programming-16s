from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class Register(generic.CreateView):

    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return settings.LOGIN_URL
