from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=100)
    telephone = models.CharField('Телефон', max_length=40)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"
