from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ImageGallery(models.Model):
    class ImageGalleryObject(models.Manager):
        def get_query(self):
            return super().get_queryset().filter(restrict_from_view=False)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    restrict_from_view = models.BooleanField(default=False)
    publishedDate = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    gelleryobjects = ImageGalleryObject()

    class Meta:
        verbose_name = "Church Gallery"
        verbose_name_plural = "Church Gallery"

    def __str__(self):
        return self.caption
