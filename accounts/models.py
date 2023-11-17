from django.db import models
from django.contrib.auth.models import User


class Mode(models.Model):
    name = models.CharField(max_length=30)
    stylesheet = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Preferences(models.Model):
    display_mode = models.ForeignKey(
        Mode,
        related_name='preferences',
        on_delete=models.PROTECT,
        null=True,
    )
    owner = models.ForeignKey(
        User,
        related_name="preferences",
        on_delete=models.CASCADE,
        null=True,
    )
