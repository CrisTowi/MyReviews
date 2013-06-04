from django.forms import ModelForm
from django import forms
from principal.models import Resena
from django.contrib.auth.models import User

class ResenaForm(forms.Form):
	mensaje = forms.CharField(widget = forms.Textarea)