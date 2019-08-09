from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    roles = (
        ('1', 'admin'),
        ('2', 'user'),
    )

    role = models.CharField(max_length=100, default=2, choices=roles)