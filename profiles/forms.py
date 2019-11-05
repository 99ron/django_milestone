from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone_number', 'street_address1', 'street_address2','town_city', 'postcode', 'country', 'image']
        
        
