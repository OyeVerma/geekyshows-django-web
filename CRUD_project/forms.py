from django import forms
from .models import StudentRegistration

class StudentRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = StudentRegistration
        fields = ("name","email", "passw")
        labels = {
            'name':'',
            'email':'',
            'passw':''
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control text-center', 'placeholder':'Enter Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control text-center', 'placeholder':'Enter Email'}),
            'passw':forms.PasswordInput(render_value=True, attrs={'class':'form-control text-center', 'placeholder':'Enter Password'})
        }
