# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]

    