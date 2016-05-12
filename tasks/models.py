from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    priority = models.IntegerField()
