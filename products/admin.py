from django.contrib import admin
from .models import Services, TypeOfService, OptionalService, Damage, WrapColour

# Register your models here.
admin.site.register(Services)
admin.site.register(TypeOfService)
admin.site.register(OptionalService)
admin.site.register(Damage)
admin.site.register(WrapColour)