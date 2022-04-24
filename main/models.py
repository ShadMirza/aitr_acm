from datetime import date
from distutils.command.upload import upload
from django.db import models
from matplotlib import image

# Create your models here.
class Event(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    venue = models.CharField(max_length=100, default='Acropolis Institue of Technology and Research, Indore')
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=250, default='')
    completed = models.BooleanField(default=False)

class Team(models.Model):
    name = models.CharField(max_length=50, blank=False)
    designation = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='team')
    acm_link = models.URLField(blank=False)
    linkedin_link = models.URLField(blank=False)
