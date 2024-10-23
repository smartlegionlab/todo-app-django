from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from my_tasks.decorators import task_owner_required
from my_tasks.forms import TaskForm
from my_tasks.models import Task


@login_required
def tasks(request):
    message = request.session.pop('message', None)
    task_list = Task.objects.filter(profile_id=request.user.id)
    context = {'tasks': task_list, 'message': message}
    return render(request, "my_tasks/tasks.html", context)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.profile = request.user
            task.save()
            message = {
                'type': 'success',
                'text': 'Task created!',
            }
            request.session['message'] = message
            return redirect('tasks:tasks')
    else:
        form = TaskForm()
    return render(request, 'my_tasks/task_form.html', {'form': form})


@login_required
@task_owner_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            message = {'type': 'success', 'text': 'Task updated!'}
            request.session['message'] = message
            return redirect('tasks:tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'my_tasks/task_form.html', {'form': form})


@login_required
@task_owner_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    try:
        task.delete()
    except Exception as e:
        print(e)
        message = {'type': 'danger', 'text': f'WARNING! Error deleting task "{task.title}"! {e}'}
    else:
        message = {'type': 'success', 'text': f'Task "{task.title}" deleted!'}
    request.session['message'] = message
    return redirect('tasks:tasks')


@login_required
@task_owner_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'my_tasks/task_detail.html', context)


@login_required
@task_owner_required
def toggle_task_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.toggle_completion()
    if task.completed:
        text = 'The task has been successfully marked as completed.!'
        type_ = 'success'
    else:
        text = 'The task is marked as NOT completed!'
        type_ = 'warning'
    message = {'type': type_, 'text': text}
    request.session['message'] = message
    return redirect('tasks:tasks')
