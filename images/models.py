import uuid

from django.core.validators import validate_ipv46_address
from django.db import models


# Create your models here.
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alt_text = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(validators=[validate_ipv46_address])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        abstract = True
