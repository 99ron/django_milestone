from django import forms
from products.models import Services

class quotesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['type_of_service', 'optional_service', 'damage', 'car_make', 'car_model', 'total_price' ]