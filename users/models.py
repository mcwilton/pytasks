from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
import os


#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name ='profile')
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    id_number = models.CharField(null=True, max_length=16)
    address = models.CharField(max_length=300, null=True)
    id_image = models.ImageField(blank=True, upload_to='media')
    address_image = models.ImageField(blank=True, upload_to='media')

    def get_upload_to(self, filename):
        folder_name = 'media'
        filename = self.file.field.storage.get_valid_name(filename)
        return os.path.join(folder_name, filename)

    def __str__(self):
        return f'{self.user.username}--Profile'