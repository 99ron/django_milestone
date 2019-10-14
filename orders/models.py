from django.db import models
from django.contrib.auth.models import User
from products.models import Services 

# Orders table.

class OrderList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=25)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.service_id.invoice_no
        
    