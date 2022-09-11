from rest_framework.serializers import ModelSerializer

import orders.models


class OrderModelSerializer(ModelSerializer):
	class Meta:
		model = orders.models.Order
		fields = '__all__'
