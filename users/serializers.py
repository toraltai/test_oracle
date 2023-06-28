from rest_framework import serializers 
from .models import Teacher
from django.contrib.auth import get_user_model
 

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    
    password_confirm = serializers.CharField()


    class Meta:
        model = User
        fields = [
            'phone_number', 'name', 'password', 
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
        fields = ['name', 'phone_number', 'grade', 'object']