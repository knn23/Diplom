from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Подключите модель User, если еще не подключена
from forum.models import Topic, Answer



@login_required
def user_statistics(request):
    user = request.user
    forum_messages_count = Topic.objects.filter(author=user).count() + Answer.objects.filter(author=user).count()

    # Получаем все задачи пользователя

    context = {
        'user': user,
        'first_login': user.date_joined,
        'last_logout': user.last_login,
        'forum_messages_count': forum_messages_count,
    }

    return render(request, 'stats/user_stats.html', context)
