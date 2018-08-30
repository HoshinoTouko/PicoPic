'''
File: serializers.py
Created Date: Thursday August 30th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 Your Company
'''
from rest_framework import serializers
from post.models import Post


class PostSerializers(serializers.ModelSerializer):
    """PostSerializers"""
    author = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('name', 'title', 'author', 'image')

    def get_author(self, obj):
        """Get author"""
        return {
            'id': obj.owner.id,
            'name': obj.owner.username,
        }

    def get_image(self, obj):
        """Get image"""
        return list(map(lambda x: x.name, obj.image.all()))
