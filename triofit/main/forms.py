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

# class Contactus(ContactUsForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Name'}), max_length=100, required=True)
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}),max_length=100, required=True)
    # mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Mobile Number'}),max_length=100, required=True)
    # comment= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Mobile Number'}),max_length=500, required=True)
    # class Meta:
    #     model = ContactUs
    #     fields = ['name','email','mobile','comment']