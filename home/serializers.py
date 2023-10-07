from rest_framework import routers, serializers, viewsets
from .models import *


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
