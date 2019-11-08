from django.db import models
from django.contrib.auth.models import User
from products.models import Services 

# Orders table.

class OrderList(models.Model):
    username = models.CharField(max_length=25)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.service_id.invoice_no
        
    