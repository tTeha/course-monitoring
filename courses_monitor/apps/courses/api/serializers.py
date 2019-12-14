from rest_framework import serializers
from ..models import Course, CourseMaterial, StudentCourses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {
            'teacher': {'read_only': True},
        }


class CourseMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = '__all__'
        extra_kwargs = {
            'course': {'read_only': True},
        }


class EnrollCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourses
        fields = '__all__'
        extra_kwargs = {
            'student': {'read_only': True},
        }
