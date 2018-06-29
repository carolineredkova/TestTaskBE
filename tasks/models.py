from django.db import models

class Task(models.Model):
    description = models.TextField()
