from django.contrib import admin
from payment.models import paymentDetails

# Registers the paymentDetails model into the admin panel.
admin.site.register(paymentDetails)