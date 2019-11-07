from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Table for the User profile

numbersOnly = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=11, validators=[numbersOnly], blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=50, blank=False)
    town_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=50, blank=False)
    employee = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile', blank=True)

    def __str__(self):
        return "{0}".format(self.user)
