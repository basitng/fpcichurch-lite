from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView,ListCreateAPIView

from .serializers import ContactSerializer,AboutSerializer,TestimonySerializer
from .models import Contact,About,Testimony

class ContactFCPI(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutFCPI(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class Testimonies(ListAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
