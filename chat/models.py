import uuid

from django.db import models


class PromptJob(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING"
        PROCESSING = "PROCESSING"
        DONE = "DONE"
        ERROR = "ERROR"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    response = models.TextField(null=True, blank=True)

    error = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
