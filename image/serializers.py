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
from image.models import Image
from constants import IMG_BASE_URL

class ImageSerializers(serializers.ModelSerializer):
    """Image serializers"""
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('title', 'post', 'url')
    
    def get_url(self, obj):
        return IMG_BASE_URL % obj.title
