from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import School, Student, Company, Jobs
from .serializers import SchoolSerializer, StudentSerializer, CompanySerializer, JobSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
# from rest_framework. import generics
# Create your views here.

# SCHOOL API
@api_view(['POST'])
def schoolCreate(request):
    serializer = SchoolSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def schoolUpdate(request,id):
    data=request.data
    school = School.objects.get(id=id)
    serializer = SchoolSerializer(school, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def schoolDelete(request,id):
    school = School.objects.get(id=id)
    school.delete()
    return Response('Deleted succesfully')

@api_view(['GET'])
def schoolList(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def schoolDetail(request, id):
    school = School.objects.get(id=id)
    serializer = SchoolSerializer(school, many=False)
    return Response(serializer.data)
    
# class SchoolList(generics.ListCreateAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# STUDENT API
class studentCreate(APIView):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser together in order to fully support HTML form data."
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)              

@api_view(['PUT'])
def studentUpdate(request,id):
    data=request.data
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def studentDelete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response('Deleted succesfully')

@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentDetail(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def studentSchoolDetail(request, slug):
    school = School.objects.get(slug=slug)
    students = Student.objects.filter(campus=school)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)    


# COMPANY API
@api_view(['POST'])
def companyCreate(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def companyUpdate(request,id):
    data=request.data
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company, data=request.data)
    # serializer = CompanySerializer(instance=company, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def companyDelete(request,id):
    company = Company.objects.get(id=id)
    company.delete()
    return Response('Deleted succesfully')

@api_view(['GET'])
def companyList(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def companyDetail(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)

#JOBS API
@api_view(['POST'])
def jobCreate(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def jobUpdate(request,id):
    data=request.data
    job = Jobs.objects.get(id=id)
    serializer = JobSerializer(job, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def jobDelete(request,id):
    job = Jobs.objects.get(id=id)
    job.delete()
    return Response('Deleted succesfully')

@api_view(['GET'])
def jobList(request):
    jobs = Jobs.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def jobDetail(request, id):
    job = Jobs.objects.get(id=id)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def jobCompanyDetail(request, slug):
    company = Company.objects.get(slug=slug)
    jobs = Jobs.objects.filter(posted_by=company)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)  