# Generated by Django 3.1.7 on 2021-04-08 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_orderplaced_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='province',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='zipcode',
        ),
    ]
