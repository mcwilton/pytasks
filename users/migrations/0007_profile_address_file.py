# Generated by Django 3.2.8 on 2021-10-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_address_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_file',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
