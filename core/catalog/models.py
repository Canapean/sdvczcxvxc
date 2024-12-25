from django.db import models


class GroupCategory(models.Model):
    title = models.CharField(
        max_length=128
    )

    slug = models.SlugField(
        max_length=128,
        unique=True
    )

    code = models.PositiveSmallIntegerField()


class Category(models.Model):
    title = models.CharField(
        max_length=128
    )

    slug = models.SlugField(
        max_length=128,
        unique=True
    )

    subcategory = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    group_cat = models.ForeignKey(
        to=GroupCategory,
        on_delete=models.CASCADE
    )
