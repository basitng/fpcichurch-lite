from rest_framework import serializers
from general.models import News
from blog.models import ImageGallery

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','excerpt','content','status', 'caption', 'published', 'image')

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = ('id','caption','restrict_from_view','image')