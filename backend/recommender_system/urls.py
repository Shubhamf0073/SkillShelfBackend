from django.urls import path
from recommender import views

urlpatterns = [
    path('recommend/', views.recommend, name='recommend'),
]