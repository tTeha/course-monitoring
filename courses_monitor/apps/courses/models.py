from django.conf import settings
from django.db import models

# Create your models here.


class Course(models.Model):
    DEVELOPMENT = 'development'
    DESIGN = 'design'
    BUSINESS = 'business'
    MAJORS_CHOICES = [
        (DEVELOPMENT, 'development'),
        (DESIGN, 'design'),
        (BUSINESS, 'business'),
    ]
    name = models.CharField(max_length=500)
    time = models.FloatField()
    seats = models.IntegerField()
    short_description = models.CharField(max_length=500)
    main_img = models.ImageField(upload_to='images/')
    majors = models.CharField(choices=MAJORS_CHOICES, max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseMaterial(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    file1 = models.FileField(upload_to='files/')


class StudentCourses(models.Model):
    student = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name
