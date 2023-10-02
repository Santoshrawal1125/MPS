from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', About.as_view(), name='about'),
    path('shop/', Shop.as_view(), name='shop'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-details/<int:id>', BlogDetails.as_view(), name='blog-details'),
    path('contact-us/', ContactView.as_view(), name='contact'),
    path('login-register/', LoginRegister.as_view(), name='login'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('product/<slug>', ProductDetails.as_view(), name='product'),

]
