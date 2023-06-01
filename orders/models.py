from django.db import models
from inventory.models import Product
from accounts.models import Customer
from django.utils.translation import gettext_lazy as _

class OrderStatus(models.TextChoices):
        PENDING = "P", _("Pending")
        APPROVED = "A", _("Approved")
        ISSUED = "I", _("Issued")
        CANCELLED = "C", _("Cancelled")

class Order(models.Model):
    order_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    cart = models.ManyToManyField(Product, related_name="orders")
    date = models.DateTimeField()
    status = models.CharField(choices=OrderStatus.choices,max_length=3, default=OrderStatus.ISSUED)
    
