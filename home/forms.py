from django import forms
from .models import Customer
from newsletter.models import Subscription

class Sign_Up(forms.ModelForm):
    class Meta:
        model = Customer

        fields = ['name', 'email', 'password','address']

class Subscribe_Newsletter(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email_field', 'subscribe_date']
