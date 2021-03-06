from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'account/signup.html'