from django.urls import path, include
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register('', views.CoursesList)
urlpatterns = [
    path('courses/', include(r.urls)),
]
