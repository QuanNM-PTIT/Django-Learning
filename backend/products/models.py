from django.db import models

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.9)
