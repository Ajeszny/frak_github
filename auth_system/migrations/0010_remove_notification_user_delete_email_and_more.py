# Generated by Django 4.1.7 on 2023-05-25 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0009_email_alter_lessonplan_participants_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
