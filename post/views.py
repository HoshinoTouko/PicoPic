'''
File: views.py
Created Date: Wednesday August 29th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 Your Company
'''
from rest_framework import viewsets

from post.models import Post
from post.serializers import PostSerializers


# API
class PostViewSet(viewsets.ModelViewSet):
    """Post viewset"""
    queryset = Post.objects.all()
    serializer_class = PostSerializers
