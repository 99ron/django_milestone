from django.conf.urls import url, include
from django.contrib import admin
from .views import contact

# URLpatterns for the contact us app.
urlpatterns = [
    url(r'^message/$', contact, name="contact"),
]