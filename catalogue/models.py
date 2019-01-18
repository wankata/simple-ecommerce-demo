from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True,
                            verbose_name="Parent category")

    class Meta:
        unique_together = ("title", "parent")
        verbose_name_plural = "Categories"
