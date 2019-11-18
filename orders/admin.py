from django.contrib import admin
from .models import OrderList

# Registering the OrdersList to the admin panel.
admin.site.register(OrderList)