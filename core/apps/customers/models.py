from uuid import uuid4

from django.db import models

class Customer(models.Model):
    phone = models.CharField(
        verbose_name="Phone number",
        max_length=20
    )
    token = models.CharField(
        verbose_name="User token",
        max_length=255,
        default=uuid4,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name="created at",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="updated at",
        auto_now=True,
    )
    def __str__(self):
        return self.phone
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"