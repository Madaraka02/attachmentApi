from rest_framework import serializers
from .models import School, Student, Company, Jobs


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # campus_name = serializers.RelatedField(source='campus', read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField()
    # campus_name = serializers.RelatedField(source='campus', read_only=True)
    class Meta:
        model = Jobs
        fields = '__all__'        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'            