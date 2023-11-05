from django.contrib import admin, redirects
from django.urls import path
from .views import secret_messages_inbox, compose_message, all_inbox, message_detail


urlpatterns = [
    path("", secret_messages_inbox, name='inbox_list'),
    path("compose", compose_message, name='compose'),
    path("board/", all_inbox, name="board"),
    path("detail/<int:id>/", message_detail, name="detail")
]
