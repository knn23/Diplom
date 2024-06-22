from django.contrib.auth.models import User
from django.db import models


class ForumMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class TaskSolution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-solved_at']


# statistics/models.py

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля, если нужны
    # ...

    def count_forum_messages(self):
        return self.user.forummessage_set.count()

    def count_task_solutions(self):
        return self.user.tasksolution_set.count()


# Подключаем профиль пользователя к модели User
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
