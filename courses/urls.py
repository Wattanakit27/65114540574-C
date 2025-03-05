from django.urls import path
from .views import search_course_by_name

urlpatterns = [
    path("", search_course_by_name, name="search-course-by-name"),
]
