from django.urls import path
from .views import Testimonies,ContactFCPI,AboutFCPI


app_name = "general_api"
urlpatterns = [
    path("about/", AboutFCPI.as_view(), name="about_api"),
    path("testimony/", Testimonies.as_view(), name="testimonies_api"),
    path("contact/", ContactFCPI.as_view(), name="contact_api"),
]