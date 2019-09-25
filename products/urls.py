from django.conf.urls import url, include
from django.contrib import admin

from products.views import get_quote

urlpatterns = [
    url(r'^quotes/$', get_quote, name="quotes"),
]