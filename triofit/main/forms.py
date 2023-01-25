from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm

from .models import User, Contact
from django import forms
class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}), max_length=50, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}), max_length=50, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}), max_length=50, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}), max_length=50, required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter your Name','class': 'con'}),
            'email': forms.TextInput(attrs={'placeholder':'Enter your Email','class': 'con'}),
            'message': forms.TextInput(attrs={'placeholder':'Enter your Message','class': 'con2'}),
        }