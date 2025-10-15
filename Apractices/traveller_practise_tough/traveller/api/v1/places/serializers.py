from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from places.models import Place, Like,Gallery

class PlaceSerializers(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['id', 'name', 'Catogory', 'like_count', 'liked_by_user']

    def get_like_count(self, instance):
        return Like.objects.filter(place=instance, like_button=True).count()

    def get_liked_by_user(self, instance):
        user = self.context.get('request').user
        if user.is_authenticated:
            return Like.objects.filter(place=instance, user=user, like_button=True).exists()
        return False



class GallerySerializers(ModelSerializer):
    class Meta:
        fields = ("id","name")
        model = Gallery



class PlaceDetailSerializers(ModelSerializer):

    category = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()

    class Meta:
        fields = ("id","name","featured_image","place","description","catogory","gallery")
        model = Place
        

    def get_category(self, instance):
        return instance.category.name
    
    def get_gallery(self, instance):
        request = self.context.get('request')
        images = Gallery.objects.filter(place=instance)
        serializer  = GallerySerializers(images, many=True,context={"request":request})
        return serializer.data
    

