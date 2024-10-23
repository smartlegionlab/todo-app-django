from enum import Enum
from django.db import models

from profiles.models import Profile


class Priority(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=[(tag.name, tag.value) for tag in Priority],
        default=Priority.MEDIUM.name,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
