from django.contrib import admin
from django.urls import path, include
from .views import StudentAPI
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register('student', StudentAPI)

urlpatterns = [
    path('api/all_list/', include(r.urls)),
    path('api/grade/', include(r.urls)),
    path('api/school/', include(r.urls)),
]