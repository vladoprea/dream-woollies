from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        # Exclude all fields that are added or calculated automatically
        exclude = ['order_number', 'date', 
                   'delivery_cost', 'order_total', 
                   'grand_total']