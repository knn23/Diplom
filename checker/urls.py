from django.urls import path
from . import views
from .views import easy_tasks

urlpatterns = [
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('easy_tasks/', easy_tasks, name='easy_tasks'),
]
