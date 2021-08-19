from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=2000)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=1000)
    reg_no = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    transcript = models.FileField()
    year_of_completion = models.CharField(max_length=100)
    campus = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.reg_no

