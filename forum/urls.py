from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='forum'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]
