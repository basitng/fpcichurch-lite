from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView,ListCreateAPIView

from .serializers import ContactSerializer,TestimonySerializer, AboutSerializer
from .models import Contact,Testimony, About

class ContactFCPI(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutFCPI(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class Testimonies(ListAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
