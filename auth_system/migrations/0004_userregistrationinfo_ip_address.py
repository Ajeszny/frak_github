# Generated by Django 4.1.7 on 2023-05-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0003_userregistrationinfo_login_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistrationinfo',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
