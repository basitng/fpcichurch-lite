from rest_framework import serializers
from general.models import News

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','excerpt','content','status','published', 'image')

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','caption','restrict_from_view','image')