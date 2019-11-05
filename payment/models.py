from django.db import models
from django.core.validators import RegexValidator
from orders.models import OrderList
from profiles.models import UserProfile

# Payment Model.

numbersOnly = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')


class paymentDetails(models.Model):
    order = models.ForeignKey(OrderList, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, null=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=11, validators=[numbersOnly], blank=False )
    country = models.CharField(max_length=50, blank=False )
    postcode = models.CharField(max_length=50, blank=False )
    town_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False )
    
    
    def __str__(self):
        return "{0} --- Paid: {1}".format(self.order.service_id.invoice_no, self.order.paid)