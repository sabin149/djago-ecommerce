# Generated by Django 3.1.7 on 2021-04-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20210416_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default='static/profileimages/rog.jpg', upload_to='profileimages'),
        ),
    ]