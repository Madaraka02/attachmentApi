from rest_framework import serializers
from .models import School, Student, Company, Jobs


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    campus_name = serializers.RelatedField(source='campus.name', read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'name', 'reg_no', 'password', 'course', 'transcript', 'year_of_completion', 'campus_name')

class JobSerializer(serializers.ModelSerializer):
    company = serializers.RelatedField(source='posted_by.name', read_only=True)
    # campus_name = serializers.RelatedField(source='campus', read_only=True)
    class Meta:
        model = Jobs
        fields = ('id', 'title', 'description', 'required_skills', 'open', 'company')       

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'            