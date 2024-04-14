from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(validators=[MinValueValidator(limit_value=datetime.date.today)])
    time = models.TimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='events')

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='staff')

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
