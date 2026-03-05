from django.contrib import admin

from .models import teacher
from .models import unit

# Register your models here.
admin.site.register(teacher)
admin.site.register(unit)