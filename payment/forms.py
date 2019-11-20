from django import forms
from payment.models import paymentDetails

# This is the form for the stripe payment system
class makePaymentForm(forms.Form):
    
    # Makes a range for the month and year choices. 
    # Will need to be updated in the future.
    month_choices = [(i, i) for i in range(1, 12)]
    year_choices = [(i, i) for i in range( 2017, 2036)]
    
    credit_card_number = forms.CharField(label="Credit card number", required=False)
    cvv = forms.CharField(label="Security code (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=month_choices, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=year_choices, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# This form is for the user details which gets auto-filled from the user profile model.
class orderForm(forms.ModelForm):
    class Meta:
        model = paymentDetails
        fields = ['full_name', 'phone_number', 'country', 'postcode',  'town_city', 'street_address1', 'street_address2']
        
        
