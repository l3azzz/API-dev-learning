from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from places.models import Posts,Reply

class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ("id","date","post","is_submitted")
    
class UploadReplaySerializer(ModelSerializer):

    username = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = ("id","username","date","replay","is_submitted")

    def get_username(self, instance):
        return instance.username.name

class UploadPostSerializer(ModelSerializer):

    replay = UploadReplaySerializer()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ("id","username","date","post","is_submitted")

    def get_username(self, instance):
        return instance.username.name
    