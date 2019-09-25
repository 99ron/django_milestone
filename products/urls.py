from django.conf.urls import url, include
from django.contrib import admin

from products.views import get_qoute

urlpatterns = [
    url(r'^qoutes/$', get_qoute, name="qoute"),
]