from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Course


def hello(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("<h1>About page</h1>")


def courses(request):
    course = Course.objects.all()
    return render(request, "courses.html", {"courses": course})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "course_detail.html", {"course": course})


def new_course(request):
    if request.method == "POST":
        title = request.POST.get("title")
        level = request.POST.get("level")
        lessons = request.POST.get("lessons")

        if title and level and lessons:
            project = Course(title=title, level=level, lessons=lessons)
            project.save()

        return redirect("courses")
    return render(request, "new_course.html")


def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect("courses")
