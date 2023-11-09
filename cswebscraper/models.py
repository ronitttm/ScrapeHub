from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    tag1 = models.CharField(max_length=200, default="Null")
    tag2 = models.CharField(max_length=200, default="Null")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"