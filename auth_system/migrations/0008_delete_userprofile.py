# Generated by Django 4.1.7 on 2023-05-24 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0007_userprofile_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]