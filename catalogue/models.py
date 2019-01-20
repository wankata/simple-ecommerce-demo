from django.db import models

from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator

from easy_thumbnails.fields import ThumbnailerImageField


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True,
                            verbose_name=_('Parent category'))

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'parent')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    price = MoneyField(max_digits=13,
                       decimal_places=4,
                       validators=[MinMoneyValidator(0)])
    description = models.TextField(blank=True)
    image = ThumbnailerImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'category')
