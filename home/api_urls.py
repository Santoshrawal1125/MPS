from django.urls import path, include
from .api_views import *

# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]