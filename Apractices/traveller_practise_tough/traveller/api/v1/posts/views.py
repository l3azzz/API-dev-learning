from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from places.models import Posts, Reply
from api.v1.posts.serializers import PostSerializer, UploadPostSerializer, UploadReplaySerializer


@api_view(["GET"])
def post(request):
    instances = Posts.objects.all()
    serializer = PostSerializer(instances, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_post(request, pk):
    posts = Posts.objects.filter(pk=pk).first()
    reply = Reply.objects.filter(pk=pk).first()

    if posts:
        posts.is_submitted = True
        posts.save()

        context = {
            "request": request
        }
        post_serializer = UploadPostSerializer(instance=posts, context=context)

        if reply:
            reply.is_submitted = True
            reply.save()

            reply_serializer = UploadReplaySerializer(instance=reply, context=context)

            response_data = {
                "status_code": 6000,
                "message": "Post and Reply submitted successfully!",
                "post_data": post_serializer.data,
                "reply_data": reply_serializer.data,
            }
        else:
            response_data = {
                "status_code": 6000,
                "message": "Post submitted successfully (no reply found).",
                "post_data": post_serializer.data,
            }
    else:
        response_data = {
            "status_code": 6001,
            "error": "Post not found."
        }

    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_replay(request, pk):
    reply = Reply.objects.filter(pk=pk).first()

    if reply:
        reply.is_submitted = True
        reply.save()

        context = {
            "request": request,
        }
        serializer = UploadReplaySerializer(instance=reply, context=context)

        response_data = {
            "status_code": 6000,
            "message": "Reply submitted successfully!",
            "data": serializer.data,
        }
    else:
        response_data = {
            "status_code": 6001,
            "error": "Reply not found."
        }

    return Response(response_data)
