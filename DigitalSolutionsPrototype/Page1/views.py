from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .models import unit
from .forms import InputForm

def index(request):
    teach = teacher.objects.all()
    units = unit.objects.all()
    return render(request, "Page1/index.html", {'content': teach, 'unit': units})

def unitInformation(request):
    return render(request, 'Page1/unitInformation.html')

def settings(request):
    return render(request, 'Page1/settings.html')

def input(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = InputForm()

    return render(request, "Page1/input.html", {"form": form})