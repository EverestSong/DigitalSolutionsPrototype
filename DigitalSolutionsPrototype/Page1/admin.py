from django.contrib import admin

from .models import Teacher
from .models import Student
from .models import Unit 

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Unit)