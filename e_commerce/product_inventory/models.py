from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.helper_models import BaseModel


class SKU(BaseModel):
	name = models.CharField(unique=True, max_length=50)
	display_name = models.CharField(unique=True, max_length=50)
	price = models.DecimalField(decimal_places=2, max_digits=12)
	quantity_in_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000000)])

	class Meta:
		db_table = 'sku'
