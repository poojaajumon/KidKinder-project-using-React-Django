# forms.py

from django import forms
from .models import Classes, Teachers

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['classes_image', 'classes_topic', 'classes_details']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['teacher_image', 'teacher_name', 'subject']
