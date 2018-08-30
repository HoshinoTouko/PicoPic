'''
File: models.py
Created Date: Wednesday August 29th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 Your Company
'''
from django.db import models

from post.models import Post


class Image(models.Model):
    """Image module"""
    name = models.CharField(unique=True, max_length=50)
    post = models.ForeignKey(Post, related_name='image', on_delete=models.CASCADE)
