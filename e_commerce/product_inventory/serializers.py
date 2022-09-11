from rest_framework.serializers import ModelSerializer

import product_inventory.models


class SKUModelSerializer(ModelSerializer):
	class Meta:
		model = product_inventory.models.SKU
		fields = [
			"name",
			"display_name",
			"price",
			"quantity_in_stock",
		]
