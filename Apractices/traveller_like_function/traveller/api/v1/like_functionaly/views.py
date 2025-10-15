from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from places.models import Like
from api.v1.like_functionaly.serializers import LikeSerialzer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def like_history(request):
    instances = Like.objects.all()
    serializers = LikeSerialzer(instances, many=True)

    return Response(serializers.data)




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def like(request):
    instances = Like.objects.all()

    if instances.exists():
        like_func = instances.first()
        like_func.like_button = True
        like_func.save()

        context = {
            "request": request
        }
        serializer = LikeSerialzer(like_func, context=context)
        like_count = Like.objects.filter(like_button=True).count()
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
            "total_likes": like_count,
        }
        return Response(response_data)
    else:
    
        like_func = Like.objects.create(like_button=True)
        serializer = LikeSerialzer(like_func, context=context)
        context = {
            "request": request
        }
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
            "total_likes": 1, 
        }
        return Response(response_data)









