from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import teacher
from .models import unit

def index(request):
    teach = teacher.objects.all()
    units = unit.objects.all()
    return render(request, "Page1/index.html", {'content': teach, 'unit': units})

def unitInformation(request):
    return render(request, 'Page1/unitInformation.html')

def settings(request):
    return render(request, 'Page1/settings.html')