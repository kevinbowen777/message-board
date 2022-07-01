from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.text[:50]
