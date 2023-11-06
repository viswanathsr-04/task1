from django.db import models
import datetime


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
