from django import forms
from .models import teacher
from .models import student

from django.db import models

class InputForm(forms.ModelForm):
    class Meta: 
        model = teacher
        fields = ['Name', 'Email', 'Area']

class StudentForm(forms.ModelForm):
    subjectChoices = [("Specialist Mathematics", "Specialist Mathematics"), ("Specialist Methods", "Specialist Methods"), 
                      ("Mathematical Methods", "Mathematical Methods"), ("Mathematical Applications", "Mathematical Applications")]

    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 100, unique=True)
    DateOfBirth = forms.DateField()
    Subjects = models.CharField(choices = subjectChoices, null = True, blank = True, max_length = 30) 

    class Meta:
        model = student
        fields = ['Name', 'Email', 'DateOfBirth', 'Subjects']
