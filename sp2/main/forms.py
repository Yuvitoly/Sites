from dataclasses import fields
from .models import Task
from django.forms import ModelForm, TextInput, Textarea, widgets
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Введите название'}),
                   "task": forms.Textarea(attrs={'class': 'from-control', 'placeholder': 'Введите описание'})
                   }

