from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    unit_cost = models.DecimalField(max_digits=40, decimal_places=2)
    sales_price = models.DecimalField(max_digits=20, decimal_places=2)
    qty_on_hand = models.IntegerField()
    qty_reserved = models.IntegerField(default=0)
    # unit_of_measurement = models.CharField(max_length=) m mm length 

    # uom

    def __str__(self):
        return f"{self.name}"
    
    @property
    def in_stock(self):
        return self.stock_count > 0
    
    def total_qty(self):
        return self.qty_on_hand + self.qty_reserved
