from django.conf.urls import url
from django.contrib import admin
from payment.views import checkout, payment

urlpatterns = [
    url(r'^(?P<order_id>\d+)', checkout, name="checkout"),
    url(r'^payment/(?P<order_id>\d+)', payment, name="payment"),
    ]