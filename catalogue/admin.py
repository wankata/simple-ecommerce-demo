from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import Category, Product

admin.site.register(Category,
                    DraggableMPTTAdmin,
                    list_display=(
                        'tree_actions',
                        'indented_title'
                    ),
                    list_display_links=(
                        'indented_title',))

admin.site.register(Product,
                    list_display=('title', 'price', 'category'),
                    list_filter=(('category', TreeRelatedFieldListFilter),))
