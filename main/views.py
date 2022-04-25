from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    return render(request,'index.html', {'team': models.Team.objects.filter(designation='Web Master') | models.Team.objects.filter(designation='Web Developer') })
def indexacmw(request):
    return render(request,'indexacmw.html', {'team': models.Team.objects.filter(gender='F')})
def events(request):
    return render(request,'events.html', {'events': models.Event.objects.all()})
def team(request):
    return render(request,'acm-team.html', {'mentors': models.Mentor.objects.all(), 'team': models.Team.objects.all()})
