# from django.urls import path
# from recommender import views

# urlpatterns = [
#     path('recommend/', views.recommend, name='recommend'),
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recommender.urls')),
]