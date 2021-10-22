from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    ### phone = PhoneNumberField(null=False, blank=False, unique=True)
   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    id_number = models.CharField(null=True, max_length=16)
    address = models.CharField(max_length=300, null=True)
    id_file = models.FileField(upload_to='proof_docs')
    address_file = models.FileField(upload_to='proof_docs')

    def __str__(self):
        return f'{self.user.username}--Profile'