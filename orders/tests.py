from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from products.models import Services
from .models import OrderList
# Tests for the Orders App

class Orders_App_Tests(TestCase):
    
    # Confirms user will be redirected to login if not logged in.
    def test_view_order_url(self):
         page = self.client.get(reverse('orders'), follow=True)
         self.assertEquals(page.status_code, 200)
         self.assertTemplateUsed(page, 'login.html')
    
    # Confirms the URL is correct.
    def test_delete_order_url(self):
        url = reverse('delete', args=[1, 'Aaron'])
        self.assertEqual(url, '/orders/delete/1Aaron/')
    

class Orders_Models_Tests(TestCase):
    
    def test_order_table_entry(self):
        # Start an instance of Services
        sv = Services()
        sv.save()
        
        # Fill out the Order List table and compare.
        ol = OrderList(username="User", service_id=sv, paid=True)
        ol.save()
        self.assertEquals(ol.username, "User")
        self.assertEquals(ol.service_id, sv)
        self.assertEquals(ol.paid, True)
    
    
    