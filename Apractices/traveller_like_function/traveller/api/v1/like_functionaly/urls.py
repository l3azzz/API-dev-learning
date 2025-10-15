from django.urls import path,include
from api.v1.like_functionaly import views


urlpatterns = [
    path('',views.like_history),
    path('like/',views.like)
    
]