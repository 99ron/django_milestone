from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .forms import userProfileForm

# Tests for the Profiles App

class Profiles_App_Tests(TestCase):
    
    # Checks the URL is correct and as annon gets redirected.
    def test_profile_url_correct(self):
         page = self.client.get(reverse('quotes'), follow=True)
         self.assertEquals(page.status_code, 200)
         self.assertTemplateUsed(page, 'login.html')
        
    
class Profiles_Form_Tests(TestCase):
    
    # Checks that the forms validates.
    def test_profile_form_is_valid(self):
        form_data = {'full_name' : 'James Smith', 'phone_number' : 176548932, 'street_address1' : 'street1', 'street_address2' : 'street2', 'town_city' : 'town', 'postcode' : 'po2099d', 'country' : 'country', 'image' : 'image.jpg'}
        form = userProfileForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # Checks that the forms fails if something's missed.
    def test_profile_form_is_invalid(self):
        form_data = {'full_name' : 'James Smith', 'phone_number' : 176548932, 'street_address1' : 'street1', 'street_address2' : 'street2', 'town_city' : 'town', 'postcode' : '', 'country' : 'country', 'image' : 'image.jpg'}
        form = userProfileForm(data=form_data)
        self.assertFalse(form.is_valid())


class Profiles_Model_Tests(TestCase):    
    
    # This checks the model that it submits properly.
    def test_models_entry(self):
        # Sets a User instance.
        user1 = User()
        user1.save()
        
        up = UserProfile(
            user=user1,
            full_name="bob smith",
            phone_number=134256748,
            street_address1="test1",
            street_address2="test2",
            postcode="po2099",
            town_city="town",
            country="Country",
            employee=False,
            image="image.jpg"
        )
        up.save()
        
        self.assertEqual(up.user, user1)
        self.assertEqual(up.full_name, "bob smith")
        self.assertEqual(up.phone_number, 134256748)
        self.assertEqual(up.street_address1, "test1")
        self.assertEqual(up.street_address2, "test2")
        self.assertEqual(up.postcode, "po2099")
        self.assertEqual(up.town_city, "town")
        self.assertEqual(up.country, "Country")
        self.assertEqual(up.employee, False)
        self.assertEqual(up.image, "image.jpg")