from django.conf.urls import url
from django.contrib import admin
from payment.views import checkout, payment

#URLpatterns for the payment app.
urlpatterns = [
    url(r'^(?P<order_id>\d+)', checkout, name="checkout"),
    url(r'^payment/(?P<order_id>\d+)', payment, name="payment"),
    ]