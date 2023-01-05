from django.contrib import admin

from .models import Testimony,About,Contact

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('story','id', 'title')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','content')
    list_editable = ['content']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','message', 'phone')
