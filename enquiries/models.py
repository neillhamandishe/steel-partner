from django.db import models
from inventory.models import Product
from accounts.models import Customer

class Quotation(models.Model):
    customer = models.ForeignKey(Customer, related_name="enquiries")
    quotation_number = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    cart = models.ManyToManyField(Product, related_name="enquiries", on_delete=models.DO_NOTHING)

    def __str__(self):
        return "" 
