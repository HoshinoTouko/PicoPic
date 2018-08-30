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
import random
import string

from post.models import Post


class Image(models.Model):
    """Image module"""
    title = models.CharField(max_length=50, blank=True)
    post = models.ForeignKey(Post, related_name='image', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='image', null=False)

    def save(self, *args, **kwargs):
        if self.title == '':
            self.title = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        super().save(*args, **kwargs)
