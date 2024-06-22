from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('checker/', include('checker.urls')),
    path('news/', include('news.urls')),
    path('stats/', include('stats.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('', user_views.user_login, name='home'),  # Перенаправление на страницу входа
]
