from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register('student', StudentAPI)

urlpatterns = [
    path('api/all_list/', include(r.urls)),
    path('api/grade/', GradeCreateAPI.as_view()),
    path('api/school/', SchoolCreateAPI.as_view()),
    path('api/postman/', PostmanAPI.as_view()),
]