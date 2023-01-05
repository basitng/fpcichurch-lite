from django.urls import path
from .views import GalleryList, PostList, PostDetail

app_name = "blog_api"
urlpatterns = [
    path("blogs/", PostList.as_view(), name="listcreate"),
    path("blogs/<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("gallery/", GalleryList.as_view(), name="gallery_listcreate"),
    path("gallery/<int:pk>/", GalleryList.as_view(), name="gallery_detailcreate"),
]