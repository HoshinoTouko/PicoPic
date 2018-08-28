from django.contrib import admin
from image.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'post',
    )

admin.site.register(Image, ImageAdmin)
