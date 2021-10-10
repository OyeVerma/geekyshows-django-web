from typing import cast
from django import forms
from django.forms import widgets

from .models import User

class MainForm(forms.Form):
    first_name = forms.CharField(min_length=5, max_length=10, strip=True)
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())

class SearchForm(forms.Form):
    search = forms.CharField()

class UserForm(forms.ModelForm):

    # overide any model form field atrribute to form not backend
    name = forms.CharField(required=False)
    
    class Meta:
        model = User

        # arrange in front end forms
        fields = ["name",'site', "email", "password"]

        # label each field of model into front end form
        # same as help_text as error_messages
        labels = {
            'name':'Enter Your First Name',
            'email':'Enter Your Email',
            'site':'Enter Your Website',
            'password':'Enter Yoyt Pass'
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'border border-danger'}),
            'password':forms.PasswordInput
        }


