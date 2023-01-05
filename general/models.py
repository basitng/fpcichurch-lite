from django.db import models
from django.utils import timezone
# Create your models here.
class About(models.Model):
    content= models.TextField()
    
    def __str__(self):
        return self.content

class Testimony(models.Model):
    title = models.CharField(max_length=200)
    story = models.TextField()
    picture = models.ImageField(null=True, blank=True, upload_to="testimonies/images/")
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.story

    class Meta:
        verbose_name = "Testimony"
        verbose_name_plural = "Testimonies"

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    message = models.TextField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return  f"{self.fullname} Dropped a message"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
