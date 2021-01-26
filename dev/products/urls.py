from dev.products.views import (
    product_detail_view,
    product_create_view,
    product_update_view,
    dynamic_delete_view,
    product_list_view
    )
from django.urls import path

app_name = 'products'
urlpatterns = [
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', dynamic_delete_view, name='product-delete'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-list'),
    path('', product_list_view, name='product-list'),
]
