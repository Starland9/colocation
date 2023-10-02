from .models import Room, RoomImage
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = []
        
        


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        exclude = ["room"]
