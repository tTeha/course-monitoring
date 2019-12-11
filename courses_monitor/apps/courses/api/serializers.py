from rest_framework import serializers
from ..models import Course, StudentCourses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {
            'teacher': {'read_only': True},
        }


class EnrollCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourses
        fields = '__all__'
        extra_kwargs = {
            'student': {'read_only': True},
        }
