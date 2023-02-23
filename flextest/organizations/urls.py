from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Autherization.as_view()),
    path('signup/', regester),
    path('profile/edit/', edit_profile),
    path('users/all', get_users),
    path('users/<int:id>', get_users),
    path('organization/create', create_organization),
    path('organization/all', get_organizations),

]