from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from .forms import contactForm


# Tests for the Contact Us Page

class Contact_Us_Tests(TestCase):
    
    # Checks that the function to go 'contact' is working.
    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

class Contact_Form_Test(TestCase):
    
    # Checks for a valid form submission
    def test_contact_form_valid(self):
        form_data = {'from_email': 'user@testing.com', "from_name": "user", 'subject' : 'test subject', 'message' : 'test message to try'}
        form = contactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # Checks for an invalid form submission
    def test_contact_form_invalid(self):
        form_data = {'from_email': '', "from_name": "user", 'subject' : 'test subject', 'message' : 'test message to try'}
        form = contactForm(data=form_data)
        self.assertFalse(form.is_valid())