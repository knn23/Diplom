from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    description = models.TextField()
    expected_output = models.TextField()
    conditions = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS, default='easy')

    def __str__(self):
        return self.description

class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    code = models.TextField()
    is_correct = models.BooleanField(default=False)
    is_solved = models.BooleanField(default=False)  # Добавлено поле для отслеживания решения

    def __str__(self):
        return f"Solution for task: {self.task.id}"
