from django.urls import path
from .views import front

app_nmae = "frontend"

urlpatterns = [
    path("", front, name = "front")
]