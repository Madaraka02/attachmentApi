from django.contrib import admin
from .models import School, Student, Company, Jobs

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Jobs)