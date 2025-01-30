from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username