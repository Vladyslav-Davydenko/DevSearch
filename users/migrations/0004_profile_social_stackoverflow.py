# Generated by Django 4.1.1 on 2022-10-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]