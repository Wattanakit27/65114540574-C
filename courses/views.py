from django.shortcuts import render
from .models import Course

def search_course_by_name(request):
    query = request.GET.get("q", "")
    results = Course.objects.filter(course_name__icontains=query) if query else []
    return render(request, "search_course.html", {"results": results})
