from django.db import models

# Create your models here.
class Discount(models.Model):
    discount_code = models.CharField(max_length=15, unique=True)
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    used = models.BooleanField(default=False) 
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.discount_code
    
    def is_valid(self):
        return self.active and not self.used
