from django.contrib import admin

from .models import Pastor

@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):
    list_display = ("id","name", "pub_date", "role")

 