from django import forms
from .models import Teacher
from .models import Student

from django.db import models

class TeacherForm(forms.ModelForm):
    class Meta: 
        model = Teacher
        fields = ['Name', 'Email', 'Area']

class StudentForm(forms.ModelForm):
    subjects = [('Mathematical Applications', 'Mathematical Applications'), 
                ('Mathematical Methods', 'Mathematical Methods'),
                ('Specialist Methods', 'Specialist Methods'), 
                ('Specialist Mathematics', 'Specialist Mathematics')]

    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 100, unique=True)
    DOB = forms.DateField()
    Subjects = models.CharField(choices = subjects, null = True, blank = True, max_length = 30) 

    class Meta:
        model = Student
        fields = ['Name', 'Email', 'DOB', 'Subjects']
