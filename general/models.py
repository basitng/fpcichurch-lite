from django.db import models
from django.utils import timezone
from blog.models import Category
from django.contrib.auth.models import User

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
        
class News(models.Model):
    class NewsObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    slug = models.SlugField(max_length=255, unique_for_date="published")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    excerpt = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    status =models.CharField(max_length=20, choices=options, default="published")
    objects = models.Manager() #default manager
    postobjects = NewsObjects() #custom manager
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    image = models.ImageField(upload_to='blog_images/', blank=True,null=True)

    class Meta:
        ordering = ["-published"]
        verbose_name = "Latest News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

class Testimony(models.Model):
    title = models.CharField(max_length=200)
    testifier = models.CharField(max_length=200)
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
