from django.db import models


# Create your models here.
class Course(models.Model):
    """
    Model representing a course.
    """

    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    lessons = models.IntegerField()
