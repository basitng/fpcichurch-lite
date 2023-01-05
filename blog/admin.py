from django.contrib import admin
from . import models
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'status', 'slug', 'author')
    prepopulated_fields = { 'slug':('title',), }

admin.site.register(models.Category)

@admin.register(models.ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ("id","caption", "image", "restrict_from_view")
    list_editable =("restrict_from_view", "image")