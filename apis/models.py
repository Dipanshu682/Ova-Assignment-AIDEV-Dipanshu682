from django.db import models

# Create your models here.

class Reminder(models.Model):
    date = models.DateTimeField()
    message = models.TextField()