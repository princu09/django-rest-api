from rest_framework.serializers import ModelSerializer
from .models import *

class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"