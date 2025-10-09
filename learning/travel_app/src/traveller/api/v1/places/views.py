from rest_framework.response import Response
from rest_framework.decorators import api_view



from api.v1.places.serializers import PlaceSerializer, PlaceDetailSerializer
from places.models import Place

@api_view(['GET'])

def places(request):
    instances = Place.objects.filter(is_deleted=False)
    serializer = PlaceSerializer(instances, many=True, context={"request":request})
    response_data = {
        "status_code": "6000",
        "data" : serializer.data
    }
    return Response(response_data)




@api_view(['GET'])

def place(request,pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)
        serializer = PlaceDetailSerializer(instance, many=False, context={"request":request})
        response_data = {
            "status_code": "6000",
            "data" : serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": "6001",
            "message" : "Place not found"
        }
        return Response(response_data)