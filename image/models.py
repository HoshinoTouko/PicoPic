from django.db import models

from post.models import Post


class Image(models.Model):
    name = models.CharField(unique=True, max_length=50)
    post = models.ForeignKey(Post, related_name='image', on_delete=models.CASCADE)
