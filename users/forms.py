from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label="Enter first name", max_length=50)
    second_name = forms.CharField(label="Enter last name", max_length=100)
    email = forms.EmailField(label="Enter email", max_length=50)
    phone = PhoneNumberField()
    id_number = forms.CharField()
    address = forms.CharField(label="Enter address", max_length=200)
    id_file  = forms.ImageField()
    address_file  = forms.ImageField() 


    class Meta:
        model = User
        fields = ['username', 'first_name', 'second_name', 'email', 'phone', 'id_number', 'address','password1', 'password2', 'id_file', 'address_file']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']#,'first_name', 'second_name', 'phone', 'id_number', 'address', 'id_file', 'address_file']

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email']#'first_name', 'second_name', 'phone', 'id_number', 'address', 'id_file', 'address_file']
