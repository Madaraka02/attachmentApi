from django.contrib import admin
from django.urls import path
from .views import (schoolList, schoolDetail, schoolCreate, schoolUpdate, schoolDelete,
                    studentList, studentDetail, studentCreate, studentUpdate, studentDelete,
                    studentSchoolDetail)

urlpatterns = [
    # scholol api

    path('api/v1/schools/add/', schoolCreate, name='school-create'),
    path('api/v1/schools/', schoolList, name='schools'),
    path('api/v1/schools/<str:id>/', schoolDetail, name='school-detail'),
    path('api/v1/schools/update/<str:id>/', schoolUpdate, name='school-update'),
    path('api/v1/schools/delete/<str:id>/', schoolDelete, name='school-delete'),

    # student api

    path('api/v2/students/add/', studentCreate, name='student-create'),
    path('api/v2/students/', studentList, name='students'),
    path('api/v2/students/<str:id>/', studentDetail, name='student-detail'),
    path('api/v2/students/school/<str:slug>/', studentSchoolDetail, name='student-school-detail'),
    path('api/v2/students/update/<str:id>/', studentUpdate, name='student-update'),
    path('api/v2/students/delete/<str:id>/', studentDelete, name='student-delete'),
]