from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name='post', on_delete=models.SET_NULL, null=True)
