from rest_framework import serializers 
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .models import Teacher

 

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    
    password_confirm = serializers.CharField()


    class Meta:
        model = User
        fields = [
            'phone_number', 'username', 'password', 
            'password_confirm', 'grade', 'object'
        ]

    def validate_phone(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('User with this phone already exists')
        return phone_number
    

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Password does not match'
            )
        return attrs
    

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'phone_number', 'grade', 'object']


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, phone_number):
        if not User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Пользователь не зарегестрирован!')
        return Response('Успешно')

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(username=phone_number, password=password)
            if not user:
                raise serializers.ValidationError("Неправильный логин или пароль!")
            attrs['user'] = user
            return attrs