# Generated by Django 3.2.8 on 2021-10-24 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address_file',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_file',
        ),
    ]
