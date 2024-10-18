from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# def todo_list(request):
#     # todos = Todo.objects.filter(user=request.user)
#     todos = Todo.objects.all()
#     return render(request, 'todo_list.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        todo = Todo(title=title, user=request.user)  # Save with the logged-in user

        todo.save()
        return redirect('todo_list')
    return render(request, 'add_todo.html')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')

def toggle_todo_completion(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed  # Toggle the completed status
    todo.save()
    return redirect('todo_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('todo_list')


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)  # Filter todos by the logged-in user
    return render(request, 'todo_list.html', {'todos': todos})

