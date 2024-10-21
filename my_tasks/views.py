from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from my_tasks.models import Task


@login_required
def tasks(request):
    message = request.session.pop('message', None)
    task_list = Task.objects.filter(profile_id=request.user.id)
    context = {'tasks': task_list, 'message': message}
    return render(request, "my_tasks/tasks.html", context)
