from django.contrib import admin
from django.urls import path
from .views import secret_messages_inbox, compose_message

urlpatterns = [
    path("", secret_messages_inbox, name='inbox_list'),
    path("compose", compose_message, name='compose'),
]
