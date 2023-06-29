from rest_framework import status, generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


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


class LoginApi(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response('Вы вышли из своего аккаунта')
        except:
            return Response(status=403)