from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
import requests

from api.v1.places.serializers import PlaceSerializer, PlaceDetailSerializer
from places.models import Place
import json



@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):

    email = request.data['email']
    password = request.data['password']
    name = request.data['name']

    print("email", email)
    print("password", password)
    print("name", name)


    if not User.objects.filter(username=email).exists():
    
        context = {
            "request": request
        }

        User.objects.create_user(
            username=email,
            password=password,
            first_name=name
        )
        
        headers = {
            "Conent-Type": "application/json"
        }
        # data = f'"username": "{email}", "password": "{password}", "name": "{name}"'
        # final_data = "{" + data + "}"
        data = {
            "username": email,
            "password": password
        }
       
        protocol = "http://"
        if request.is_secure():
            protocol = "https://"
        host = requests.get_host()
        url = protocol + host +  "localhost:8000/api/v1/auth/token/"
        
        response = requests.post(url, headers = headers , data= json.dumps(data))

        if response.status_code == 200:
            response_data = {
                "status_code": 6000,
                "data": response.json(),
                "message": "Account created successfully",
            }
        else : 
            response_data = {
                "status_code": 6002,
                "data": "Error in obtaining token",
            }
        response_data = {
            "status_code": 6000,
            "data": "User created successfully"
        }
    else: 

         response_data = {
            "status_code": 6001,
            "data": "User Exists"
        }
    return Response(response_data)