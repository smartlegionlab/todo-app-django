from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'due_date', 'created_at', 'profile', 'get_priority_display', 'priority')
    list_filter = ('completed', 'priority', 'profile')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_editable = ('completed', 'priority')

    def get_priority_display(self, obj):
        return obj.priority.capitalize()


admin.site.register(Task, TaskAdmin)
