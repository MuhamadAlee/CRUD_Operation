from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    job = models.CharField(max_length=255)
    age = models.IntegerField()