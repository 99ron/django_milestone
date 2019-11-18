from django.contrib import admin
from .models import Reviews, Attachment

# Adding models below to the django admin panel.

admin.site.register(Reviews)
admin.site.register(Attachment)