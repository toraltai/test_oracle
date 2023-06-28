from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("Email is required")

        # email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("This is already required")
        
        # email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Teacher(AbstractUser):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    grade = models.CharField(max_length=20, verbose_name='Класс')
    object = models.CharField(max_length=20, verbose_name='Предмет')

    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.username}'
    