from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models import ForumMessage, TaskSolution


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # Создаем или обновляем запись о последнем входе пользователя
    user.last_login = timezone.now()
    user.save()


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    # Создаем или обновляем запись о последнем выходе пользователя
    user.last_logout = timezone.now()
    user.save()
