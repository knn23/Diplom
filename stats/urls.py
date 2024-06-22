# stats/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('user-stats/', views.user_statistics, name='user_stats'),
    # Другие пути по необходимости
]
