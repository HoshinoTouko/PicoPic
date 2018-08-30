'''
File: services.py
Created Date: Thursday August 30th 2018
Author: Touko Hoshino
-----
Last Modified:
Modified By:
-----
Copyright (c) 2018 HoshinoTouko
'''
import os

from image.models import Image

IMAGE_DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/image')
IMAGE_PATH = '%s/%s.%s'


class ImageService:
    """Image services"""
    @classmethod
    def retrive_image(cls, image):
        """Retrive image from data"""
        if not isinstance(image, Image):
            raise Exception('Image type error')

        img_path = IMAGE_PATH % (image.post.name, image.name, image.img_type)
        image_file_path = os.path.join(IMAGE_DATA_PATH, img_path)

        if not os.path.exists(image_file_path):
            raise Exception('Image not found %s' % image_file_path)

        with open(image_file_path, 'rb') as img_file:
            return img_file.read()

        raise Exception('Unknown error')
