from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'owner',
    )

admin.site.register(Post, PostAdmin)
