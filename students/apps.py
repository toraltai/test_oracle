from django.apps import AppConfig
# from .models import Student


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    # def ready(self):
    #     import students.