from django.db import models

from core.catalog.models import Category


class Product(models.Model):
    title = models.CharField(
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        max_length=64,
        unique=True
    )

    external_id = models.CharField(
        max_length=64,
        unique=True
    )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=8
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
