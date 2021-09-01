from rest_framework import serializers
from .models import School, Student, Company


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    campus_name = serializers.RelatedField(source='campus', read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'name', 'reg_no', 'course', 'transcript', 'year_of_completion', 'campus_name')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'            