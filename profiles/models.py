from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Table for the User profile

numbersOnly = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=30, blank=False, verbose_name="Full Name")
    phone_number = models.CharField(max_length=11, validators=[numbersOnly], blank=False, verbose_name="Phone Number")
    street_address1 = models.CharField(max_length=40, blank=False, verbose_name="Street Address 1")
    street_address2 = models.CharField(max_length=40, blank=False, verbose_name="Street Address 2")
    postcode = models.CharField(max_length=50, blank=False, verbose_name="Postcode")
    town_city = models.CharField(max_length=40, blank=False, verbose_name="Town/City")
    country = models.CharField(max_length=50, blank=False, verbose_name="Country")
    employee = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile', blank=True)

    def __str__(self):
        return "{0}".format(self.user)
