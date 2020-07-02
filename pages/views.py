from django.views.generic import *

class HomePage(TemplateView):
    template_name = 'home.html'