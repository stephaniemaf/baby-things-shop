from django.db import models
from django.utils.translation import ugettext_lazy as _
from newsletter_subscription.models import SubscriptionBase

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    address = models.TextField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    
    def __str__(self):
       return self.name

class Subscription(SubscriptionBase):
    email = models.EmailField(_('email address'), unique=True)