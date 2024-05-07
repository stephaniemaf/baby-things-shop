from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "ordered"), (1, "delivered"))
QUANTITY_AMOUNT = ((0, '0'),(1, '1'),(2, '2'),(3, '3'),(4, '4'))

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
       return self.name


class Order_history(models.Model):
    
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    name = models.CharField(max_length=254, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    address = models.TextField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(choices=QUANTITY_AMOUNT, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
       return self.name

class Delivery(models.Model):
    order = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=255)
    delivery_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Delivery {self.id} for Order #{self.order_id}"

