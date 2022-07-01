from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Default custom user model for django-start template project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    name = models.CharField("Name of User", blank=True, max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField("Bio", blank=True)

    def __str__(self):
        return self.username
