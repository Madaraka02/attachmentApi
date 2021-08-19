from django.shortcuts import render
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.decorators import api_view
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
@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

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