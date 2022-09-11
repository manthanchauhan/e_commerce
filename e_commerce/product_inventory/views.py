from rest_framework import viewsets
from rest_framework import permissions

import product_inventory.serializers
from product_inventory.models import SKU


class SKUViewSet(viewsets.ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = product_inventory.serializers.SKUModelSerializer
    permission_classes = [permissions.IsAuthenticated]
