from django.conf.urls import url, include
from django.contrib import admin

from .views import contact, successView

urlpatterns = [
    url(r'success/', successView, name='success'),
    url(r'^message/$', contact, name="contact"),
]