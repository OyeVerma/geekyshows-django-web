from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # password1 = forms.CharField
    # password2 = forms.CharField(attrs={'placeholder':'Password (Again)'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LogInForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = '__all__',
        