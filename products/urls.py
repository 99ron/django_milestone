from django.conf.urls import url, include
from django.contrib import admin

from products.views import get_quote, edit_quote

# URLpatterns for the products app.
urlpatterns = [
    url(r'^quotes/$', get_quote, name="quotes"),
    url(r'^edit-order/(?P<order_id>\w+)', edit_quote, name="edit"),
   #url(r'^edit-order/update/(?P<order_id>\w+)', update_quote, name="update"),
    ]