# Generated by Django 4.1.2 on 2022-10-21 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
    ]
