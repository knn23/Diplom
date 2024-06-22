from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name='Groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='User permissions', blank=True,                                          related_name='custom_user_permissions')
    pass
