from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views

# Tests for the home app.

class Home_App_Tests(TestCase):
    
    # This test confirms that the home page can be found.
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    # This test confirms that the about us page can be found.   
    def test_about_us_page(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    