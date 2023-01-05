from django.urls import path
from . import views
app_name = "pastors"

urlpatterns = [
    path("", views.ListPastors.as_view(), name="pastors_listcreate" ),
    path("<int:pk>/", views.DetailPastors.as_view(), name="pastors_detailretrieve" )
]