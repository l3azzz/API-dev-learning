from django.urls import path
from api.v1.posts import views

urlpatterns = [
    path('', views.post),
    path('upload/<int:pk>/', views.upload_post),
    path('upload_replay/<int:pk>/', views.upload_replay),
    
]
