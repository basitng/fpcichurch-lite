from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView

from blog.models import ImageGallery
from general.models import News as Post
from blog_api.serializers import GallerySerializer, PostSerializer

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer   

class GalleryList(ListCreateAPIView):
    queryset = ImageGallery.gelleryobjects.all()
    serializer_class = GallerySerializer
    

class GalleryDetail(RetrieveDestroyAPIView):
    queryset = ImageGallery.objects.all()
    serializer_class = GallerySerializer    

