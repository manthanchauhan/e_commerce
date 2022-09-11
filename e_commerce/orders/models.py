from decimal import Decimal

from django.db import models
from rest_framework.fields import JSONField

import product_inventory.models
from utils.helper_models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(BaseModel):
	STATUS_CHOICES = (
		("INITIATED", "Initiated"),
		("SUCCESS", "Success"),
		("FAIL", "Failed"),
		("CANCELLED", "Cancelled"),
		("REFUNDED", "Refunded")
	)

	order_status = models.CharField(choices=STATUS_CHOICES, default="INITIATED", max_length=255)
	total_amount = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
	extra_details = JSONField()

	user_id = models.PositiveIntegerField(db_index=True)
	# fulfilment_id = models.IntegerField(null=True)
	# refund_id = models.CharField(null=True, max_length=255, blank=True)

	class Meta:
		db_table = 'order'


class OrderItem(BaseModel):
	order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='items')
	sku = models.ForeignKey(to=product_inventory.models.SKU, on_delete=models.RESTRICT, related_name='+')
	quantity = models.PositiveIntegerField(validators=[MaxValueValidator(1000000000)])
	unit_price = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1000000000)])


class OrderPayment(BaseModel):
	PAYMENT_MODES = [
		(0, 'CC'),
		(1, 'DC'),
		(2, 'UPI'),
	]

	PAYMENT_PARTNERS = [
		(0, 'Razor Pay'),
		(1, 'Bill Desk'),
	]

	PAYMENT_STATUS = [
		(0, 'Initiated'),
		(1, 'Success'),
		(2, 'Fail'),
		(3, 'Refunded'),
	]

	order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='payments')
	payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODES)
	payment_partner = models.CharField(max_length=50, choices=PAYMENT_PARTNERS)
	partner_txn_id = models.CharField(unique=True, max_length=50)
	amount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1000000000)])
	partner_txn_status = models.CharField(max_length=50)
	status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
