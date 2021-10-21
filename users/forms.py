from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label="Enter first name",max_length=50)
    second_name = forms.CharField(label="Enter last name",max_length=100)
    email = forms.EmailField(label="Enter email",max_length=50)
    mobile = PhoneNumberField()
    address = forms.CharField()
    id_file  = forms.FileField() 
    address_file  = forms.FileField() 


    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',  'email']

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']