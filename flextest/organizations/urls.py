from django.contrib import admin
from django.urls import path
from .views import Autherization

urlpatterns = [
    path('login/', Autherization.as_view()),
]