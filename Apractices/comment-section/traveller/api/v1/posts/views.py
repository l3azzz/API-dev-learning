from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from places.models import Posts
from api.v1.posts.serializers import PostSerializer, UploadPostSerializer


@api_view(["GET"])
def post(request):
    """
    Get all posts.
    """
    instances = Posts.objects.all()
    serializer = PostSerializer(instances, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_post(request, pk):
    posts = Posts.objects.filter(pk=pk)

    if posts.exists():
        post = posts[0]
        post.is_submitted = True
        post.save()

        context = {"request": request}
        serializer = UploadPostSerializer(instance=post, context=context)

        response_data = {
            "status_code": 6000,
            "message": "Post submitted successfully!",
            "data": serializer.data
        }
    else:
        response_data = {
            "status_code": 4004,
            "error": "Post not found."
        }

    return Response(response_data)
