from rest_framework import viewsets
from rest_framework import permissions
from orders.models import Order
from orders.serializer import OrderModelSerializer


class OrderViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Order.objects.all()
	serializer_class = OrderModelSerializer

	def create(self, request, *args, **kwargs):
		return super(OrderViewSet, self).create(request, *args, **kwargs)
