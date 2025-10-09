from django.urls import path
from . import views

urlpatterns = [
    path('', views.places),
    path('view<int:pk>/', views.place),
]
