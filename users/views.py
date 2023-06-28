from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import RegisterSerializer, TeacherSerializer


User = get_user_model()

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Account created', 201)
        
        
class TeacherListAPI(generics.ListAPIView):
    queryset= Teacher.objects.all()
    serializer_class = TeacherSerializer
