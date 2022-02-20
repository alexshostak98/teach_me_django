from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, related_name="profile")
    phone = models.CharField(
        max_length=16,
        validators=(
            RegexValidator(regex=r"^\+?\d{8,15}$", message="Неверный телефонный номер"),
        ),
        blank=True,
        null=True,
    )
    bio = models.TextField(null=True, blank=True)
    github = models.URLField(max_length=2048, null=True, blank=True)
