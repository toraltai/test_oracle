from rest_framework.viewsets import ModelViewSet
from rest_framework import views, generics, decorators, response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .signals import message_handler

class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'second_name']


class GradeCreateAPI(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class SchoolCreateAPI(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class PostmanAPI(views.APIView):
    def post(self, request):
        print(request.data['text'])
        students = Student.objects.all()
        for student in students:
            message_handler(student.mail, student.first_name, student.second_name, request.data['text'])
        return response.Response('Postman mission done')