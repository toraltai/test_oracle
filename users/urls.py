from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/register/', RegisterAPIView.as_view()),
    path('api/list/', TeacherListAPI.as_view()),
    path('login/', LoginApi.as_view()),
    path('logout/', LogoutApi.as_view()),
]