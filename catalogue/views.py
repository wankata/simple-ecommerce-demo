from django.views.generic import DetailView
from .models import Category


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_object().product_set.all()
        return context
