# Generated by Django 3.1.7 on 2021-04-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20210414_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imageb',
        ),
    ]
