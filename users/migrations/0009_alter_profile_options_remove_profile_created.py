# Generated by Django 4.1.1 on 2023-01-07 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_options_profile_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-name']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
    ]
