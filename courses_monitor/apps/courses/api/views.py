# Rest Framework
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import CourseSerializer, EnrollCoursesSerializer
from ..models import Course, StudentCourses


class CoursesList(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseLCView(ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(teacher_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        posted_data = serializer.validated_data
        posted_data['teacher_id'] = self.kwargs['pk']
        # print(posted_data['teacher_id'])
        return serializer.save()


class CourseRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(teacher_id=self.kwargs['spk'])


class EnrollCoursesCreateView(ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = EnrollCoursesSerializer

    def get_queryset(self):
        return StudentCourses.objects.filter(student_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        posted_data = serializer.validated_data
        posted_data['student_id'] = self.kwargs['pk']
        return serializer.save()


class EnrollCoursesRUDView(RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EnrollCoursesSerializer

    def get_queryset(self):
        return StudentCourses.objects.filter(student_id=self.kwargs['spk'])


class StudentCoursesListView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = CourseSerializer

    def get_queryset(self):
        courses_list = StudentCourses.objects.filter(student_id=self.kwargs['pk'])
        if courses_list.exists():
            courses_list_ids = [course.course_id for course in courses_list]
            courses = Course.objects.filter(id__in=courses_list_ids)
            return courses
        return None


class StudentCourseRetrieveView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CourseSerializer

    def get_queryset(self):
        courses_list = StudentCourses.objects.filter(student_id=self.kwargs['spk'])
        if courses_list.exists():
            courses_list_ids = [course.course_id for course in courses_list]
            courses = Course.objects.filter(id__in=courses_list_ids)
            return courses
        return None
