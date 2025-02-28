from django.urls import path
from .views import AddProduct, DeleteProduct, ProductDetails, UpdateProduct, homeView, aboutView, contactsView, searchView

urlpatterns = [
    path("", homeView, name="home"),
    path("about", aboutView, name="aboutpage"),
    path("contacts", contactsView, name="contactpage"),

    path("products/add", AddProduct.as_view(), name = "addproduct"),                  # C
    path("products/<int:pk>", ProductDetails.as_view(), name = "prod_details"),        # R
    path("products/edit/<int:pk>", UpdateProduct.as_view(), name = "edit_prod"),    # U
    path("products/del/<int:pk>", DeleteProduct.as_view(), name = "del_prod") ,      # D


    # search path
    path('products/search', searchView, name = 'search')
]
