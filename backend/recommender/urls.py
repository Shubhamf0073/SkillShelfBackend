from django.urls import path
from .views import CourseList, RecommendCourse

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('recommend/', RecommendCourse.as_view(), name='recommend-course'),
]