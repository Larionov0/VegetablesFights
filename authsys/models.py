from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leaves = models.IntegerField(default=0, help_text='Деньги')

    def __str__(self):
        return f"{self.user.username}"
