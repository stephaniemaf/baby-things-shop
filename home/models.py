from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    address = models.TextField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    
    def __str__(self):
       return self.name

