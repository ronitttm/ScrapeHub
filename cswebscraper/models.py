from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    tag1 = models.CharField(max_length=200, default="Null")
    tag2 = models.CharField(max_length=200, default="Null")

    def _str_(self):
        return self.title