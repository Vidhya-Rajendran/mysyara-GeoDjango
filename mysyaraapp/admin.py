# Register your models here.
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Washer, CarWashOrders

@admin.register(Washer)
class WasherAdmin(OSMGeoAdmin):
    list_display = ('washer_shop_name', 'current_location', 'is_available')

@admin.register(CarWashOrders)
class NewOrder(OSMGeoAdmin):
    exclude=['assigned_to']
    washer_name = CarWashOrders.objects.filter(assigned_to__is_available=1)
    list_display = ('customer_name', 'customer_location', 'car_no', 'washer_name')
