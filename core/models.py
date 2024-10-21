from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class AppSetting(SingletonModel):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
