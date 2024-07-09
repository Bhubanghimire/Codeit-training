from django.urls import path,include
from products.views import product, create, category_list, category_create
from products.views import GenericCategory, CategoryDetailView, CategoryUpdateView, category_delete


urlpatterns = [
    path("", product, name="product_list"),
    # path('category-create', category_create, name="cat_create"),
    path("create",create, name="product_create"),
    # path("category-list",category_list, name="category_list")
    path("generic-category-list/", GenericCategory.as_view(), name="category_list"),
     path("category/<int:pk>/detail/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/<int:pk>/update/", CategoryUpdateView.as_view(), name="category_update"),
    path("category/<int:pk>/delete/", category_delete, name="category_delete"),
]