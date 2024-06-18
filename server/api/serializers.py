from rest_framework import serializers
from .models import Student, Teachers ,Classes

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'teacher_image', 'teacher_name', 'subject']

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'classes_image', 'classes_topic', 'classes_details']

