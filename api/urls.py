from django.contrib import admin
from django.urls import path
from .views import (schoolList, schoolDetail, schoolCreate, schoolUpdate, schoolDelete,
                    studentList, studentDetail, studentCreate, studentUpdate, studentDelete,
                    studentSchoolDetail,
                    companyList, companyDetail, companyCreate, companyUpdate, companyDelete,
                    jobCreate, jobUpdate, jobDelete, jobList, jobDetail, jobCompanyDetail, getStudentLogins)

urlpatterns = [
    # school api

    path('api/v1/schools/add/', schoolCreate, name='school-create'),
    path('api/v1/schools/', schoolList, name='schools'),
    path('api/v1/schools/<str:id>/', schoolDetail, name='school-detail'),
    path('api/v1/schools/<str:id>/update/', schoolUpdate, name='school-update'),
    path('api/v1/schools/<str:id>/delete/', schoolDelete, name='school-delete'),

    # student api

    path('api/v2/students/add/', studentCreate.as_view(), name='student-create'),
    path('api/v2/students/', studentList, name='students'),
    path('api/v2/students/credentials/', getStudentLogins, name='students-login'),
    path('api/v2/students/<str:id>/', studentDetail, name='student-detail'),
    path('api/v2/students/school/<str:slug>/', studentSchoolDetail, name='student-school-detail'),
    path('api/v2/students/<str:id>/update/', studentUpdate, name='student-update'),
    path('api/v2/students/<str:id>/delete/', studentDelete, name='student-delete'),

    # company api

    path('api/v3/companies/add/', companyCreate, name='company-create'),
    path('api/v3/companies/', companyList, name='companyies'),
    path('api/v3/companies/<str:id>/', companyDetail, name='company-detail'),
    path('api/v3/companies/<str:id>/update/', companyUpdate, name='company-update'),
    path('api/v3/companies/<str:id>/delete/', companyDelete, name='company-delete'),

    #Jobs api

    path('api/v4/jobs/add/', jobCreate, name='job-create'),
    path('api/v4/jobs/', jobList, name='jobs'),
    path('api/v4/jobs/<str:id>/', jobDetail, name='job-detail'),
    path('api/v4/jobs/company/<str:slug>/', jobCompanyDetail, name='job-company-detail'),
    path('api/v4/jobs/<str:id>/update/', jobUpdate, name='job-update'),
    path('api/v4/jobs/<str:id>/delete/', jobDelete, name='job-delete'),
]