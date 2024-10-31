from functools import wraps

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from .models import Task


def task_owner_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.profile != request.user:
            messages.error(request, 'WARNING! Error deleting task! Task not found...')
            return redirect('tasks:tasks')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
