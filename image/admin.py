from django.contrib import admin
from image.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'post',
        'image',
    )

admin.site.register(Image, ImageAdmin)
