from django.conf.urls import url
from payment.views import checkout

urlpatterns = [
    url(r'^$', checkout, name="checkout"),
    ]