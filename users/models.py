from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Booking(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_full_name = models.CharField(max_length=255)
    company = models.CharField(max_length= 255)
    email_id = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=False, blank=False)
    is_pick_them_up = models.BooleanField()
    enable_chain_custody = models.BooleanField()
    pickup_date = models.DateField()
    single_location = models.BooleanField()




class ShippingLocation(models.Model):
    address_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=False, blank=False)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    ingestion_center = models.CharField(max_length=255)
    user_id = models.ForeignKey("Booking",  on_delete=models.CASCADE, related_name='locations')

