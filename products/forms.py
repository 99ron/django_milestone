from django import forms
from products.models import Services

class quotesForm(forms.ModelForm):
    class Meta:
        model = Services
        exclude = ('type_of_service', 'optional_service', 'damage', 'total_price')
        fields = ['car_make', 'car_model']