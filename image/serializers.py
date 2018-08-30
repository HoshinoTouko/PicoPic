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


class ImageSerializers(serializers.ModelSerializer):
    """Image serializers"""
    class Meta:
        model = Image
        fields = ('name', 'post', 'img_type')
