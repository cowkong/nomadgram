from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    #pass  # empty class

    list_display_links = (
        'location',
        'caption',
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'creator',
    )
    list_display =(
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )
    


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'image'
    )
@admin.register(models.Comment) # 바로 붙여서 써야함 안그러면 에러남.
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )
