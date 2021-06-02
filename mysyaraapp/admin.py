# Register your models here.
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Washer, CarWashOrder

@admin.register(Washer)
class WasherAdmin(OSMGeoAdmin):
    list_display = ('washer_shop_name', 'current_location', 'is_available')

@admin.register(CarWashOrder)
class NewOrder(OSMGeoAdmin):
    # exclude=['assigned_to']
    list_display = ('customer_name', 'customer_location', 'car_no', 'get_washer')

    def get_washer(self, obj):
        return obj.assigned_to.washer_shop_name
    get_washer.admin_order_field = 'assigned_to'
    get_washer.short_description = 'Assigned To'
