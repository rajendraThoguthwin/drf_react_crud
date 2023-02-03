from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    starring = models.CharField(max_length=50)
