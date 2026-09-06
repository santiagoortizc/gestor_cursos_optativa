from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.hello),
    path("about/", views.about),
    path("courses/", views.courses, name="courses"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    path("courses/new-course/", views.new_course, name="new_course"),
    path("courses/<int:course_id>/delete", views.delete_course, name="delete_course"),
    path("courses/<int:course_id>/edit", views.edit_course, name="edit_course"),
    path("courses/<int:course_id>/new-lesson", views.new_lesson, name="new_lesson"),
]
