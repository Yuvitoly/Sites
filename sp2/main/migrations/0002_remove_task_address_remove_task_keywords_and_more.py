# Generated by Django 4.1.3 on 2022-12-08 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='address',
        ),
        migrations.RemoveField(
            model_name='task',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='task',
            name='telephone',
        ),
    ]
