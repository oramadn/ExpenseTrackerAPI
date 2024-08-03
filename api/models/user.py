from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    deleted_at = models.DateTimeField(null=True, blank=True)