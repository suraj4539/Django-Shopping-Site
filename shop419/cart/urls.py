from django.urls import path

from . import views


urlpatterns = [
    path('cart/', views.viewCart, name = 'view_cart'),
    path('cart/add/<int:product_id>', views.addToCart, name = 'add_to_cart' ),
    path('cart/remove/<int:cart_item_id>', views.remFromCart, name = 'remove_from_cart'),
    path('cart/add/<int:cart_item_id>/', views.addQuantity, name='add_quantity'),
    path('cart/remove/<int:cart_item_id>/', views.remQuantity, name='rem_quantity'),
]