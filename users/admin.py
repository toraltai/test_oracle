from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone_number']