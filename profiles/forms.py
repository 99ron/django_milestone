from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'postcode', 'country', 'image']

