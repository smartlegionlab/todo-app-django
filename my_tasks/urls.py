from django.urls import path

from . import views

app_name = 'tasks'


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('create/', views.create_task, name='task_create'),
    path('update/<int:pk>/', views.update_task, name='task_update'),
    path('delete/<int:pk>/', views.delete_task, name='task_delete'),
    path('toggle/<int:pk>/', views.toggle_task_completion, name='toggle_task_completion'),
]
