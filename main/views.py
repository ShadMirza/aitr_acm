from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    return render(request,'index.html')
def events(request):
    return render(request,'events.html', {'events': models.Event.objects.all()})
def team(request):
    return render(request,'acm-team.html')
