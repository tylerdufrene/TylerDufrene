from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('Date Created', auto_now_add=True)