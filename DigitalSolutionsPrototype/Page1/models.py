from django.db import models 
from django.utils import timezone
from django import forms

import datetime

# Create your models here.

class Teacher(models.Model):
    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 100, unique=True)
    Area = models.CharField(max_length = 40)

class Student(models.Model):
    subjects = [('Mathematical Applications', 'Mathematical Applications'), 
                ('Mathematical Methods', 'Mathematical Methods'),
                ('Specialist Methods', 'Specialist Methods'), 
                ('Specialist Mathematics', 'Specialist Mathematics')]

    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=100, unique=True)
    DOB = models.DateField(default=timezone.now)
    Subjects = models.CharField(choices=subjects, null=True, blank=True, max_length=30) 

class Unit(models.Model):
    Title = models.CharField(max_length = 50)
    Accreditation = models.CharField(max_length = 10)
    Unit_Description = models.TextField()
    Unit_Goals = models.TextField()
    Content_Descriptions = models.TextField()
