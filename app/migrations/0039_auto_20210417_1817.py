# Generated by Django 3.1.7 on 2021-04-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20210417_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='marked_price',
            field=models.IntegerField(blank=True),
        ),
    ]
