from django import forms
from django import forms
from .models import Teacher 
from .models import Student 
from .models import Unit 

from django.db import models

class TeacherForm(forms.ModelForm):
    class Meta: 
        model = Teacher
        fields = ['Name', 'Email', 'Area']

class StudentForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Unit.objects.all(), empty_label="---------") 
    DOB = forms.DateField()

    class Meta:
        model = Student
        fields = ['Name', 'Email', 'DOB', 'Subjects']
