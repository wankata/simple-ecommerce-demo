from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True,
                            verbose_name='Parent category')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'parent')
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    price = MoneyField(max_digits=13,
                       decimal_places=4,
                       validators=[MinMoneyValidator(0)])
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'category')
