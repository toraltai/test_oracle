from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Student

@receiver(post_save, sender=Student)
def student_created_signal(created, instance, *args, **kwargs):
    if created:
        send_mail(
            "Test message",
            f"Welcome {instance.first_name} {instance.second_name}. \n Привет вам",
            settings.EMAIL_HOST_USER,
            [instance.mail]
        )

def message_handler(mail:list, first_name, second_name, text):
        send_mail(
            f"Dear {first_name} {second_name}.",
            f'Good day {first_name} {second_name}, ' + text,
            settings.EMAIL_HOST_USER,
            [mail]
        )
