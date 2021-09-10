from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=2000)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    reg_no = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    transcript = models.FileField()
    year_of_completion = models.CharField(max_length=100)
    campus = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    @receiver(post_save, sender=User)
    def create_user_student(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_student(sender, instance, **kwargs):
        instance.student.save()

    

    def __str__(self):
        return self.reg_no

    class Meta:
        ordering = ('-id',) 

class Company(models.Model):
    name = models.CharField(max_length=2000)
    reg_number = models.CharField(max_length=3000)
    slug = models.SlugField()

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ('-id',)     

class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    required_skills = models.TextField()
    open = models.BooleanField(default=True)
    posted_by = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)    

class RegisterStudents(models.Model):
    username = models.CharField(max_length=)  
    password = 
    student =      