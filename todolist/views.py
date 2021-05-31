from django.shortcuts import render
from .models import Status, ToDo

def home(request):
    todos = ToDo.objects.all()
    context = {'todos': todos}
    return render(request, 'todolist/home.html', context)
