from django.db import models


# Create your models here.
class Course(models.Model):
    """
    Model representing a course.
    """

    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    lessons = models.IntegerField()

class Lesson(models.Model):
    """
    Model representing a lesson.
    """
    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons_set")
    title = models.CharField(max_length=100)
    content= models.TextField()
    duration = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')