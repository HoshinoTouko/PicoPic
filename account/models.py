from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
