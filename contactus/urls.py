from django.conf.urls import url, include
from django.contrib import admin

from .views import emailView, successView

urlpatterns = [
    url('email/', emailView, name='email'),
    url('success/', successView, name='success'),
]