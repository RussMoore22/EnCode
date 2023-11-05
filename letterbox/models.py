from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SecretMessage(models.Model):
    text = models.TextField()
    encrypted_text = models.TextField(null=True, blank=True)
    subject = models.CharField(max_length=225, null=True)
    encoder = models.CharField(max_length=20)
    date_sent = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(
        User,
        related_name='sent_messages',
        on_delete=models.CASCADE,
    )
    receipient = models.ForeignKey(
        User,
        related_name='received_messages',
        on_delete=models.CASCADE,
    )
