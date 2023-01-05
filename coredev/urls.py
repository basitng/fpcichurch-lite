from django.contrib import admin
from django.urls import include, path
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include("blog.urls", namespace="blog")),
    path('api/', include("blog_api.urls", namespace="blog_api")),
    path('api/pastors/', include("pastors.urls", namespace="pastors")),
    path('api/general/', include("general.urls", namespace="general_api")),
]

admin.site.site_header = "FCPI CHURCH"
admin.site.site_title = "FCPI CHURCH DASHBOARD"
admin.site.index_title = "Welcome to FCPI DASHBOARD"

