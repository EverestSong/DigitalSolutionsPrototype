from django.db import models

# Create your models here.

class teacher(models.Model):
    Name = models.CharField(max_length = 25)
    Email = models.CharField(max_length = 40)
    Area = models.CharField(max_length = 30)

class unit(models.Model):
    Title = models.CharField(max_length = 50)
    Accreditation = models.CharField(max_length = 10)
    Unit_Description = models.CharField(max_length = 1000)
    Unit_Goals = models.CharField(max_length = 1000)
    Content_Descriptions = models.CharField(max_length = 1000)