'''
File: models.py
Created Date: Wednesday August 29th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 Hoshino Touko
'''
from django.db import models

from post.models import Post

IMG_TYPE_CHOICES = (
    ('jpg', 'JPG/JPEG'),
    ('png', 'PNG'),
    ('gif', 'GIF'),
)


class Image(models.Model):
    """Image module"""
    name = models.CharField(unique=True, max_length=50)
    post = models.ForeignKey(Post, related_name='image', on_delete=models.CASCADE)
    img_type = models.CharField(choices=IMG_TYPE_CHOICES, default='JPG/JPEG', max_length=50)
