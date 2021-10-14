from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control text-center mt-2', 'placeholder':'Email', 'type':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control text-center mt-2', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control text-center mt-2', 'placeholder':'Password (Again)'}))
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control text-center mt-2', 'placeholder':'User Name'}),
            'first_name':forms.TextInput(attrs={'class':'form-control text-center mt-2', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control text-center mt-2', 'placeholder':'Last Name'}),

        }

        labels = {
            'username':'',
            'email':'',
            'password1':'',
            'password2':'',
     
        }
