from datetime import date
from distutils.command.upload import upload
from django.db import models
from matplotlib import image
import os

# Create your models here.
class Event(models.Model):
    date = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    venue = models.CharField(max_length=100, default='Acropolis Institue of Technology and Research, Indore')
    detail = models.CharField(max_length=250, default='')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

class Mentor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    designation = models.CharField(max_length=50, blank=False, default='Faculty Incharge')
    image = models.ImageField(upload_to=os.path.join('mentors'))
    acm_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.name 

gender = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Team(models.Model):
    name = models.CharField(max_length=50, blank=False)
    designation = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=2, choices=gender, default='M')
    acmw_designation = models.CharField(max_length=50, default='Member', blank=True)
    image = models.ImageField(upload_to=os.path.join('team'))
    acm_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.name 
