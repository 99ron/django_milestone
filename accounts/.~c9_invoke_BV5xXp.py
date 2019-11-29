from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from .froms import *

# Test for the accounts app

class Accounts_App_Tests(TestCase):
    
    # Checks that the function to go 'home' is working.
    def test_index_func(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class Setup_Class(TestCase):
    
    def setUp(self):
        # Sets up a user for testing
        self.user = User.objects.create(email="user@testing.com",        username="TestUser", password1="password", password2="password")

class Registration_Form_Test(TestCase):
    
    
    # Valid Form Data
    def test_reg_form_valid(self):
        form = UserRegistrationForm(
            
            data={'email': 'user@testing.com', "username": "user", 'password1' : 'p'})