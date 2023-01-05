from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from .serializers import PastorsSerializer

from .models import Pastor

# Create your views here.
class ListPastors(ListCreateAPIView):
    queryset = Pastor.objects.all()
    serializer_class = PastorsSerializer

class DetailPastors(RetrieveDestroyAPIView):
    queryset = Pastor.objects.all()
    serializer_class = PastorsSerializer