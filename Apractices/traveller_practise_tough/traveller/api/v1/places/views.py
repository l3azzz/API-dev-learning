from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated , AllowAny


from api.v1.places.serializers import PlaceSerializers
from places.models import Place,Catogory
from django.db.models import Q


from api.v1.places.pagination import StandardResultSetPagination

@api_view(["GET"])
def places(request):
    instance = Place.objects.filter(is_deleted=False)

    q = request.GET.get("q")
    if q:
        ids = [int(i) for i in q.split(",")]
        instance = instance.filter(Catogory__in=ids)

    paginator = StandardResultSetPagination()
    paginator_result = paginator.page_queryset(instance, request)

    serializer = PlaceSerializers(
        paginator_result, many=True, context={"request": request}
    )

    response_data = {
        "status_code": 6000,
        "count": paginator.page.paginator.count,
        "links": {
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
        },
        "data": serializer.data
    }

    return Response(response_data)


@api_view(["GET"])
def place(request, pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)
        context = {
            "request": request,
        }
        serializer = PlaceSerializers(instance=instance, context=context)  
        response_data = {
            "status_code": 6000,
            "data": serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "place not exists"
        }
        return Response(response_data)        

@permission_classes([AllowAny])
@api_view(["GET"])
def places(request):
    instance = Place.objects.filter(is_deleted=False)
    context = {
        "request":request,
    }
    serializer = PlaceSerializers(instance,many=True,context=context)
    response_data = {
        "status_code":6000,
        "data" : serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected(request, pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)
        context = {
            "request": request,
        }
        serializer = PlaceSerializers(instance=instance, context=context)  
        response_data = {
            "status_code": 6000,
            "data": serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "place not exists"
        }
        return Response(response_data)        
        