from django.contrib import admin

from .models import News, Testimony,Contact, About

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('story','id', 'title')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','message', 'phone')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','content')

@admin.register(News)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'status', 'slug', 'author', 'category')
    prepopulated_fields = { 'slug':('title',), }
