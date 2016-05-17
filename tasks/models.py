from django.db import models


class Task(models.Model):

    owner = models.ForeignKey('auth.User',
                              related_name='tasks', default=1)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(default='')
    status = models.IntegerField(
            choices=((1, 'Backlog'), (2, 'Ready'), (3, 'Doing'),
                     (4, 'Done')), blank=True)
    priority = models.IntegerField()

    class Meta:
        ordering = ('priority', )
