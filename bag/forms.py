from django import forms

class DiscountCodeForm(forms.Form):
    discount_code = forms.CharField(max_length=20, required=False)