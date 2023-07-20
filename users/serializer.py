from rest_framework import serializers
from .models import User, Booking, ShippingLocation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')

class ShippingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingLocation
        fields = ('address_id', 'full_name', 'country', 'phone_number', 'address', 'state', 'zip_code', 'ingestion_center', 'user_id')

class BookingSerializer(serializers.ModelSerializer):
    locations = ShippingLocationSerializer(many=True, read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
       
