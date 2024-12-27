from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend, name='recommend'),
    path('api/recommendations/', views.get_recommendations, name='get_recommendations'),
]