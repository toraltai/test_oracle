from django.contrib import admin
from django.urls import path, include
from .views import RegisterAPIView, TeacherListAPI
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/register/', RegisterAPIView.as_view()),
    path('api/list/', TeacherListAPI.as_view())
]