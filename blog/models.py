from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    # Post Manager 
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    # PROTECT WILL NOT ALLOW POST TO BE DELETED WHEN A CATEGORY IS DELETED 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    # SLUG IS USED TO IDEMTIFY A POST 
    slug = models.SlugField(max_length=255, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    # CASCADE MEANS WHEN A USER IS DELETED DELETE POST 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status =models.CharField(max_length=20, choices=options, default="published")
    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager
    image = models.ImageField(upload_to='blog_images/', blank=True,null=True)


    class Meta:
        ordering = ["-published"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        required_db_vendor = "sqlite, postgresql, mysql, oracle"

    def __str__(self):
        return self.title


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
