from django.contrib import admin
from .models import Mode, Preferences


@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'stylesheet',
    ]


@admin.register(Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    fields = [
        'display_mode',
        'owner',
    ]
