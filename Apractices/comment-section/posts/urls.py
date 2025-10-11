from django.urls import path ,include
from api.v1.posts import views

urlpatterns = [
    path('', views),
    

]
