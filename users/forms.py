from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label="Enter First Name", max_length=50)
    second_name = forms.CharField(label="Enter Last Name", max_length=100)
    email = forms.EmailField(label="Enter Email", max_length=50)
    phone = PhoneNumberField(label="Enter Phone Number")
    id_number = forms.CharField(label="Enter ID Number")
    address = forms.CharField(label="Enter Home Address", max_length=200)
    id_image = forms.ImageField(label="Upload ID Image", required=False)
    address_image  = forms.ImageField(label="Upload Address Image", required=False)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'second_name', 'email', 'phone', 'id_number', 'address','password1', 'password2', 'id_image', 'address_image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name'] # 'second_name', 'phone', 'id_number', 'address']

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'first_name']# 'second_name', 'phone', 'id_number', 'address']
