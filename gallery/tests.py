from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from django.utils import timezone

from .forms import reviewForm
from .models import Reviews, Attachment


# Tests for the Gallery App

class Gallery_App_Tests(TestCase):
    
    # Checks that the function to view 'gallery' is working.
    def test_gallery_page(self):
        response = self.client.get(reverse('gallery'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        
    
    # Checks the URL pattern for review more is working. 
    def test_review_more_page(self):
        url = reverse('review_more', args=[1])
        self.assertEqual(url, '/gallery/review_more/1')
    
    # Checks the URL pattern for add review is working. 
    def test_add_review_page(self):
        url = reverse('add_review', args=[1])
        self.assertEqual(url, '/gallery/add_review/1')

    
   


    