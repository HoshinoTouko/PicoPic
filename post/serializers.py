'''
File: serializers.py
Created Date: Thursday August 30th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 Hoshino Touko
'''
from rest_framework import serializers
from post.models import Post
from constants import IMG_BASE_URL


class PostSerializers(serializers.ModelSerializer):
    """Post serializers"""
    author = serializers.SerializerMethodField()
    preview_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'author', 'preview_image')

    def get_author(self, obj):
        """Get author"""
        return {
            'id': obj.owner.id,
            'name': obj.owner.username,
        }

    def get_preview_image(self, obj):
        """Get image"""
        return list(map(lambda x: IMG_BASE_URL % x.title, obj.image.all()[:9]))
