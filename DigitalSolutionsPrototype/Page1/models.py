from django.db import models

# Create your models here.

class teacher(models.Model):
    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 100, unique=True)
    Area = models.CharField(max_length = 30)

class unit(models.Model):
    Title = models.CharField(max_length = 50)
    Accreditation = models.CharField(max_length = 10)
    Unit_Description = models.CharField(max_length = 1000)
    Unit_Goals = models.CharField(max_length = 1000)
    Content_Descriptions = models.CharField(max_length = 1000)
    
class student(models.Model):
    subjectChoices = [("Specialist Mathematics", "Specialist Mathematics"), ("Specialist Methods", "Specialist Methods"), 
                      ("Mathematical Methods", "Mathematical Methods"), ("Mathematical Applications", "Mathematical Applications")] 

    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 100, unique=True)
    Subjects = models.CharField(choices = subjectChoices, null = True, blank = True, max_length = 30) 