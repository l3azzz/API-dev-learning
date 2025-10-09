from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.v1.tasks.serializers import TaskSerializer
from tasks.models import Task



@api_view(["GET"])
def tasks(request):
    instances = Task.objects.filter(is_deleted=False)
    serializer = TaskSerializer(instances , many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        response_data = {
            "status_code" : 6000,
            "message" : "Success"
        }

        return Response(response_data)
    else:

        response_data = {
            "status_code" : 6001,
            "message" : "Validation Error",
            "data" : serializer.errors
        }

        return Response(response_data)
    

@api_view(["POST"])
def update_task(request, pk):
    if Task.objects.filter(pk=pk).exists():
        instance = Task.objects.get(pk=pk)
        serializer = TaskSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "status_code" : 6000,
                "message" : "Success"
            }

            return Response(response_data)
        else:

            response_data = {
                "status_code" : 6001,
                "message" : "Validation Error",
                "data" : serializer.errors
            }

            return Response(response_data)
        

    else:

        response_data = {
                "status_code" : 6001,
                "message" : "Not Found",
            }
        return Response(response_data)



@api_view(["POST"])
def delete_task(request, pk):
    if Task.objects.filter(pk=pk).exists():
        instance = Task.objects.get(pk=pk)
        serializer = TaskSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "status_code" : 6000,
                "message" : "Success Deleted u Stupid"
            }

            return Response(response_data)
        else:

            response_data = {
                "status_code" : 6001,
                "message" : "Validation Error",
                "data" : serializer.errors
            }

            return Response(response_data)
        

    else:

        response_data = {
                "status_code" : 6001,
                "message" : "Not Found",
            }
        return Response(response_data)



