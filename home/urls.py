from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', About.as_view(), name='about'),
    path('shop/', Shop.as_view(), name='shop'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-details/<int:id>', BlogDetails.as_view(), name='blog-details'),
    path('contact-us/', ContactView.as_view(), name='contact'),
    path('signup/', signup, name='signup'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('product/<slug>', ProductDetails.as_view(), name='product'),
    path('search', SearchView.as_view(), name='search'),
    path('my-account', MyAccount.as_view(), name='account'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('reduce_cart/<slug>', reduce_cart, name='reduce_cart'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('add_to_wishlist/<slug>', add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist/<slug>', delete_wishlist, name='delete_wishlist'),
    path('product_review/<slug>', product_review, name='product_review'),
]
