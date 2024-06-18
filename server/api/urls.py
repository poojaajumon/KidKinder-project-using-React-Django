from django.urls import path,include
from . import views
from rest_framework import routers

# Create a router and register our viewsets with it
router = routers.DefaultRouter()
router.register(r'teachers', views.TeacherViewSet)
router.register(r'classes', views.ClassesViewSet)

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_view, name='login'),  # Login view
    path('logout/', views.logout_view, name='logout'),  # Logout view
    path('submit/', views.submit_booking, name='submit_booking'),  # Submit booking view
    path('bookings/', views.display_bookings, name='display_bookings'),  # Display bookings view
    path('teachers/', views.teachers, name='teachers'),  # Teachers view
    path('classes/', views.classes, name='classes'),  # Classes view
    path('add_teacher/', views.add_teacher, name='add_teacher'),  # Add teacher view
    path('api/add_teacher/', views.AddTeacherAPIView.as_view(), name='add_teacher_api'),
    path('add_class/', views.add_class, name='add_class'),  # Add class view
    path('api/add_class/', views.AddClassAPIView.as_view(), name='add_class_api'),
    path('classes/<int:pk>/edit/', views.edit_class, name='edit_class'),
    path('classes/<int:pk>/delete/', views.delete_class, name='delete_class'),
    path('teachers/<int:pk>/edit/', views.edit_teacher, name='edit_teacher'),
    path('teachers/<int:pk>/delete/', views.delete_teacher, name='delete_teacher'),
    path('api/', include(router.urls)),  # Include router URLs
]


  
    


