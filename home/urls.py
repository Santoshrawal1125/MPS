from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', About.as_view(), name='about'),
    path('shop/', Shop.as_view(), name='shop'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contact-us/', Contact.as_view(), name='contact'),
    path('login-register/', LoginRegister.as_view(), name='login'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout')

]
