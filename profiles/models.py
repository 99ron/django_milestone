from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=11)
    address = models.TextField(max_length=200)
    postcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile')
    
    def __str__(self):
        return self.user.username
    