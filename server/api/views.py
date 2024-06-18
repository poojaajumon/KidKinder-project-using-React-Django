from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .models import Teachers , Classes
from .serializers import TeacherSerializer ,ClassesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from .forms import ClassForm , TeacherForm





@csrf_exempt
def submit_booking(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            student_class = data.get('studentClass')
            booking = Student(name=name, email=email, student_class=student_class)
            booking.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False}, status=400)

def display_bookings(request):
    bookings = Student.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page or another page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

def teachers(request):
    teachers = Teachers.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

def classes(request):
    classes_data = Classes.objects.all()
    return render(request, 'classes.html', {'classes_data': classes_data})


def edit_class(request, pk):
    cls_instance = get_object_or_404(Classes, pk=pk)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES, instance=cls_instance)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = ClassForm(instance=cls_instance)
    
    return render(request, 'edit_class.html', {'form': form})


def delete_class(request, pk):
    cls = get_object_or_404(Classes, pk=pk)
    if request.method == 'POST':
        cls.delete()
        return redirect('classes')  # Redirect to the classes view after deletion
    # Handle GET request gracefully, you can also redirect to classes or render a template
    return redirect('classes')  # Redirect to the classes view for GET requests




def edit_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    teacher.delete()
    return redirect('teachers')

    

def add_teacher(request):
    return render(request, 'add_teacher.html')
class AddTeacherAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('teachers')  # Redirect to the teachers list page
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddClassAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('classes') 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def add_class(request):
    return render(request, 'add_class.html')


