from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)
    published_at = models.DateTimeField()
    url = models.URLField(default='')  # Указываем значение по умолчанию

    def __str__(self):
        return self.title
