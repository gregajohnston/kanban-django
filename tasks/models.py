from django.db import models


class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks', default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=255, blank=True, default='')
    priority = models.IntegerField()

    class Meta:
        ordering = ('priority', )
