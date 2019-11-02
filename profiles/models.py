from django.db import models
from django.contrib.auth.models import User

# Table for the User profile

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    address = models.TextField(max_length=200)
    postcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    employee = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile', blank=True)

    def __str__(self):
        return self.user.username
