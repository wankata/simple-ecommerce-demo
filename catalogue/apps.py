from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CatalogueConfig(AppConfig):
    name = 'catalogue'
    verbose_name = _('Product catalogue')
