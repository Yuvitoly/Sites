# Generated by Django 4.1.3 on 2022-12-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('telephone', models.CharField(max_length=40, verbose_name='Телефон')),
                ('keywords', models.TextField(verbose_name='Ключевые слова')),
            ],
        ),
    ]
