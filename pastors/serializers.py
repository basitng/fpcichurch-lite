from rest_framework import serializers
from .models import Pastor

class PastorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastor
        fields = ('id','name','role')
