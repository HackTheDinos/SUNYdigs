from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Word
''' STARTING ON FORMS '''



class TranslationForm(forms.Form):
    #translation = forms.CharField(widget=forms.Textarea,label="")
    translation = forms.CharField(label="")
