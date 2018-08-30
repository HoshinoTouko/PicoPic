'''
File: views.py
Created Date: Wednesday August 29th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 Hoshino Touko
'''
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
import json

from image.models import Image
from image.serializers import ImageSerializers

class ImageViewSet(viewsets.ModelViewSet):
    """Image viewset"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializers


def retrive_image(request, image_title):
    """Get image view"""
    image_instance = get_object_or_404(Image, title=image_title)

    try:
        return HttpResponse(image_instance.image, content_type="image")
    except Exception as e:
        return HttpResponse(json.dumps({'Error': str(e)}), status=403)
