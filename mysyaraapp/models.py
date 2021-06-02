# from django.db import models
from django.contrib.gis.db import models
from django.forms.models import model_to_dict
from django.contrib.gis.db.models.functions import Distance
from django.core.exceptions import ValidationError
# Create your models here.

class Washer(models.Model):
    washer_shop_name = models.CharField(max_length=100)
    current_location = models.PointField(blank=True, null=True)
    is_available = models.BooleanField(default=False, editable=False)

class CarWashOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_location = models.PointField(blank=True, null=True)
    car_no = models.CharField(max_length=20)
    assigned_to = models.ForeignKey('Washer', editable=False, null=True, on_delete=models.SET_NULL, related_name='washer_name')
    
    def save(self, *args, **kwargs):
        super(CarWashOrder, self).save(*args, **kwargs)
        dict_obj = model_to_dict(self)
        available_washer = Washer.objects.filter(is_available=0)
        nearest = available_washer.annotate(distance=Distance('current_location',
            dict_obj['customer_location'])
            ).order_by('distance').first()
        if nearest:
            updated = CarWashOrder.objects.filter(id=dict_obj['id']).update(assigned_to=nearest)
            if updated == 1:
                Washer.objects.filter(id=nearest.id).update(is_available=1)
        else:
            raise ValidationError("Sorry!! There is no washer available right now")

          
        
        