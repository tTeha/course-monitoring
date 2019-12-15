from django.urls import path, include
from rest_framework import routers

from . import views

r = routers.DefaultRouter()
r.register('', views.CoursesList)
urlpatterns = [
    path('courses/', include(r.urls)),
    path('teacher/<int:pk>/courses/', views.CourseLCView.as_view(), name="teacher_courses"),
    path('teacher/<int:spk>/course/<int:pk>/', views.CourseRUDView.as_view(), name="RUD_teacher_courses"),
    path('course/<int:pk>/materials/', views.CourseMaterialsCreateView.as_view(), name="teacher_courses_materials"),
    path('new/<int:pk>/courses/', views.NewCoursesListView.as_view(), name="new_courses"),
    path('student/<int:pk>/studentcourses/', views.EnrollCoursesCreateView.as_view(), name="add_student_courses"),
    path('student/<int:spk>/studentcourse/<int:pk>/', views.EnrollCoursesRUDView.as_view(), name="RD_student_courses"),
    path('student/<int:pk>/courses/', views.StudentCoursesListView.as_view(), name="get_a_student_courses"),
    path('student/<int:spk>/course/<int:pk>/', views.StudentCourseRetrieveView.as_view(), name="get_a_student_courses"),
]
