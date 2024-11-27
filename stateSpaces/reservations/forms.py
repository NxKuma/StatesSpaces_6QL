from django import forms

from .models import Product, Transaction


class VenueForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'stock_status': forms.Select(choices=Product.STATUS_CHOICES),
        }


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('amount', 'transaction_status')