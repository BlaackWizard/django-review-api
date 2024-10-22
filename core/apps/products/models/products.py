from django.db import models

from core.apps.products.entities.products import Product as ProductEntity


class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название заметки")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )

    def to_entity(self):
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
