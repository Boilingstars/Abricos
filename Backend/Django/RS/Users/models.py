from django.db import models
from django.contrib.auth.models import AbstractUser

# Приложение для управления данными о пользователях
class SignedUser(AbstractUser):
    license_key = models.CharField(max_length=40)

    class Meta:
        app_label = 'Users'

    def __str__(self):
        return self.username