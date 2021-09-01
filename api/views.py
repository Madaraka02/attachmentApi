from django.shortcuts import render
from rest_framework.views import APIView
from .models import School, Student, Company
from .serializers import SchoolSerializer, StudentSerializer, CompanySerializer
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

@api_view(['POST'])
def schoolUpdate(request,id):
    school = School.objects.get(id=id)
    serializer = SchoolSerializer(instance=school, data=request.data)

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
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
status=status.HTTP_400_BAD_REQUEST)               

@api_view(['POST'])
def studentUpdate(request,id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=student, data=request.data)

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

@api_view(['POST'])
def companyUpdate(request,id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(instance=company, data=request.data)

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
