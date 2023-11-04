from django.contrib import admin
from .models import SecretMessage
# Register your models here.
@admin.register(SecretMessage)
class SecretMessageAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'sender',
        'receipient',

    ]
