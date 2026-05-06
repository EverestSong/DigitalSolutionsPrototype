#from msilib.schema import File
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from .models import Teacher
from .models import Student
from .models import Unit

from .forms import TeacherForm
from .forms import StudentForm

from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO

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

def report(request):
    pdf_file = staticfiles_storage.path("DigitalSolutions.pdf")

    try:
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="attachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="noAttachment.pdf")

    return response

def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [("Name: ", "Teaching Area: ")]

    teachers = Teacher.objects.all()

    for teacher in teachers:
        lines.append((teacher.Name, teacher.Area))

    table = Table(lines)
    table.wrapOn(p, 300, 200)
    table.drawOn(p, 10, 740)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer