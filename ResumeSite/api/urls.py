from django.contrib import admin
from django.urls import path

from .models import Room
from .views import RoomView


urlpatterns = [
    path('', RoomView.as_view()),
]
