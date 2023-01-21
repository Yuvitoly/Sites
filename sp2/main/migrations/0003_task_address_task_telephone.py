# Generated by Django 4.1.3 on 2022-12-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_task_address_remove_task_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='address',
            field=models.CharField(default=1, max_length=100, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='telephone',
            field=models.CharField(default=1, max_length=40, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]