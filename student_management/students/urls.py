from django.urls import path
from .views import course_list, student_list, course_detail,register_student

urlpatterns = [
    path('register/', register_student, name='register_student'),
    path('courses/', course_list, name='course_list'),
    path('students/', student_list, name='student_list'),
    path('courses/<int:pk>/', course_detail, name='course_detail'),
]
