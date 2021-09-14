from rest_framework import serializers
from .models import School, Student, Company, Jobs


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    campus_name = serializers.CharField(source='campus.name', read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'name', 'reg_no', 'password', 'course', 'transcript', 'year_of_completion', 'campus_name')

class JobSerializer(serializers.ModelSerializer):
    # posted_by = serializers.StringRelatedField()
    company_name = serializers.CharField(source='posted_by.name', read_only=True)
    class Meta:
        model = Jobs
        fields = ('id', 'title', 'description', 'required_skills', 'open', 'company_name')        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'            

class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'reg_no', 'password')  

class SchoolLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'password')     

class CompanyLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'reg_number', 'password')                   