from django.db import models
from django.utils import timezone
from django import forms

import datetime

# Create your models here.

class Teacher(models.Model):
    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 100, unique=True)
    Area = models.CharField(max_length = 40)

class Subject(models.Model):
    Name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.Name

class Student(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=100, unique=True)
    DOB = models.DateField(default=timezone.now)
    Subjects = models.ManyToManyField(Subject, blank=True) 

class Unit(models.Model):
    Title = models.CharField(max_length = 50)
    Accreditation = models.CharField(max_length = 10)
    Unit_Description = models.TextField()
    Unit_Goals = models.TextField()
    Content_Descriptions = models.TextField()

    def __str__(self):
        return self.Title
