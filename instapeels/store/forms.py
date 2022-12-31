from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms
class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}), max_length=50, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}), max_length=50, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}), max_length=50, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}), max_length=50, required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']