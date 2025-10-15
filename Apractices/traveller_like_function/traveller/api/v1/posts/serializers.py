from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from places.models import Posts

class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ("id","date","post","is_submitted")
    

class UploadPostSerializer(ModelSerializer):

    username = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ("id","username","date","post","is_submitted")

    def get_username(self, instance):
        return instance.username.name