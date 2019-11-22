from django.contrib import admin
from .models import Services, TypeOfService, OptionalService, Damage, WrapColour

# Registering models for the admin panel
admin.site.register(Services)
admin.site.register(TypeOfService)
admin.site.register(OptionalService)
admin.site.register(Damage)
admin.site.register(WrapColour)