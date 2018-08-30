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
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
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
            if '.' in str(self.image.name):
                suffix = str(self.image.name).split('.')[-1]
                self.image.name = '%s.%s' % (self.title, suffix)
            else:
                self.image.name = self.title
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)
