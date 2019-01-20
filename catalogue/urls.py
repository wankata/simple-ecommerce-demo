from django.urls import path
from .views import CategoryDetail

urlpatterns = [
    path("category/<int:pk>/",
         CategoryDetail.as_view(),
         name="catalogue-category-detail")
]
