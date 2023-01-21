from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    task = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Список задач', 'tasks': task})


def about(request):
    task = Task.objects.all()
    return render(request, 'main/about.html', {'title': 'Информация', 'tasks': task})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


