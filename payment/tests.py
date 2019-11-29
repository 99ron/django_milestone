from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from .forms import makePaymentForm, orderForm

# Tests for the Payment app

class Payment_App_Tests(TestCase):
    
    # This test confirms that the checkout page can be found.
    def test_checkout_page(self):
        url = reverse('checkout', args=[1])
        self.assertEqual(url, '/checkout/1')
        
    # This test confirms that the payment page can be found.   
    def test_payment_page(self):
        url = reverse('payment', args=[1])
        self.assertEqual(url, '/checkout/payment/1')


class Payment_Form_Tests(TestCase):
    
    # Confirms the form validates for the payment form
    def test_payment_form_is_valid(self):
        form_data = {
            'credit_card_number' : '4242424242424242',
            'cvv' : '111',
            'expiry_month' : 3,
            'expiry_year' : 2021,
            'stripe_id' : 'something'}
            
        form = makePaymentForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # Confirms the form validates for the orders form
    def test_order_form(self):
        form_data = {
            'full_name': 'James Smith',
            'phone_number': '0775643521',
            'street_address1': '1 false drive',
            'street_address2': 'flat 3',
            'town_city': 'West City',
            'country': 'Some Country',
            'postcode': 'po2099d'
        }
        form=orderForm(data=form_data)
        self.assertTrue(form.is_valid())
