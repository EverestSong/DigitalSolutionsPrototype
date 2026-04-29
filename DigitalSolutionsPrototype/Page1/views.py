from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from .models import Teacher
from .models import Student
from .models import Unit

from .forms import TeacherForm
from .forms import StudentForm

def index(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    units = Unit.objects.all()
    return render(request, "Page1/index.html", {'teachers': teachers, 'students': students, 'units': units})

def unitInformation(request):
    return render(request, 'Page1/unitInformation.html')

def settings(request):
    return render(request, 'Page1/settings.html')

def teacherForm(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            nameInput = request.POST.get('Name', None)
            emailInput = request.POST.get('Email', None)
            areaInput = request.POST.get('Area', None)

            Teacher.objects.update_or_create(Email=emailInput, defaults = {"Name" : nameInput, "Area" : areaInput}) 

    else:
        form = TeacherForm()

    return render(request, "Page1/teacherForm.html", {'form': form})
    #return render(request, "Page1/input.html", {"form": form})

def studentForm(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            nameInput = request.POST.get('Name', None)
            emailInput = request.POST.get('Email', None)
            dobInput = request.POST.get('DOB', None)
            subjectInput = request.POST.get('Subjects', None)

            Student.objects.update_or_create(Email=emailInput, defaults = {"Name" : nameInput, "DOB": dobInput, "Subjects" : subjectInput}) 

    else:
        form = StudentForm()

    return render(request, "Page1/studentForm.html", {'form': form})