from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Message.Status.PUBLISHED)


"""
class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Message.Status.DRAFT)
"""


class Message(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        null=False,
        unique_for_date="publish",
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="message_posts",
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PUBLISHED,
    )

    objects = models.Manager()
    # draft = DraftManager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "message_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
