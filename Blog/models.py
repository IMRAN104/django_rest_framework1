from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.TextField(max_length=50)
    slug = models.SlugField(default='hello', max_length=30)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
