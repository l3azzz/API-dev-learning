from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from places.models import Like

class LikeSerialzer(ModelSerializer):
    class Meta:
        model = Like
        fields = ("id","like_button")


