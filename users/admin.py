from django.contrib import admin

from users.models import Booking, ShippingLocation
# Register your models here.


admin.site.register(Booking)
admin.site.register(ShippingLocation)