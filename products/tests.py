from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from .models import *
# Tests for the Products Page

class Products_App_Tests(TestCase):
    
    # Checks that the user is redirected to the login page if they're not logged in.
    def test_gallery_URLs_if_user_is_annon(self):
        quotes = self.client.get(reverse('quotes'), follow=True)
        quotes2 = self.client.get(reverse('edit', args=[1]), follow=True)
        quotes3 = self.client.get(reverse('update', args=[1]), follow=True)
        self.assertEquals(quotes.status_code, 200)
        self.assertEquals(quotes2.status_code, 200)
        self.assertEquals(quotes3.status_code, 200)
        self.assertTemplateUsed(quotes, 'login.html')
        self.assertTemplateUsed(quotes2, 'login.html')
        self.assertTemplateUsed(quotes3, 'login.html')
      
    
class Products_Models_Tests(TestCase):
    
    # Type of service model
    def test_type_of_service_entry(self):
        tos = TypeOfService(name="Full Wrap", image="tos.jpg", price=299)
        tos.save()
        
        self.assertEqual(tos.name, "Full Wrap")
        self.assertEqual(tos.image, "tos.jpg")
        self.assertEqual(tos.price, 299)
    
    # Wrap Colour model
    def test_wrap_colour_entry(self):
        wc = WrapColour(name="Flat Red", image="color.jpg", price=0)
        wc.save()
        
        self.assertEqual(wc.name, "Flat Red")
        self.assertEqual(wc.image, "color.jpg")
        self.assertEqual(wc.price, 0)
            
    
    # Extra Services Model
    def test_extra_services_entry(self):
        es = OptionalService(name="Door Shuts", is_needed=False, price=400)
        es.save()
        
        self.assertEqual(es.name, "Door Shuts")
        self.assertEqual(es.is_needed, False)
        self.assertEqual(es.price, 400)
    
    # Vehicle Damage Model
    def test_vehicle_damage_entry(self):
        vd = Damage(name="Front Bumper", price=0)
        vd.save()
        
        self.assertEqual(vd.name, "Front Bumper")
        self.assertEqual(vd.price, 0)
    
