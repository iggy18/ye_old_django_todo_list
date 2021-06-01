from django.shortcuts import render
from .models import Status, ToDo
from .forms import ToDoForm
from django.http import HttpResponseRedirect

def home(request):
    #post request from model form
    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        print(request.POST)
    #request
    todos = ToDo.objects.all()
    context = {'todos': todos, 'form': form}
    return render(request, 'todolist/todos.html', context)
