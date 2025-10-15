from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from places.models  import Place,Gallery

class PlaceSerializers(ModelSerializer):
    class Meta:
        fields = ("id","name","featured_image","place")
        model = Place


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