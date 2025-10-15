from django.urls import path ,include
from api.v1.places import views

urlpatterns = [
    path('', views.places),
    path('views/<int:pk>', views.place),
    path('protected/<int:pk>', views.protected),

]
