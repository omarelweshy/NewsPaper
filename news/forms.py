from django import forms
from news.models import *
class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'title', 'body', 'image',]
