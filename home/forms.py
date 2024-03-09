from django import forms
from .models import Customer

class Sign_Up(forms.ModelForm):
    class Meta:
        model = Customer

        fields = ['name', 'email', 'password','address']