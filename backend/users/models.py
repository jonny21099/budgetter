from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True, primary_key=True)

    USERNAME_FIELD = 'username'