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

from image.models import Image
from image.serializers import ImageSerializers
from image.services import ImageService

class ImageViewSet(viewsets.ModelViewSet):
    """Image viewset"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializers


def retrive_image(request, image_name):
    """Get image view"""
    image_instance = get_object_or_404(Image, name=image_name)

    return HttpResponse(ImageService.retrive_image(
        image_instance), content_type="image/%s" % image_instance.img_type)
