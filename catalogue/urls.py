from django.urls import path
from .views import CategoryDetail, ProductDetail

urlpatterns = [
    path("category/<int:pk>/",
         CategoryDetail.as_view(),
         name="catalogue-category-detail"),
    path("product/<int:pk>/",
         ProductDetail.as_view(),
         name="catalogue-product-detail")

]
