# Generated by Django 3.1 on 2020-08-18 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manageapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='V_no',
        ),
    ]
