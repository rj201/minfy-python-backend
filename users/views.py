from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializer import UserSerializer, BookingSerializer, ShippingLocationSerializer
from rest_framework.response import Response

from .models import User, Booking, ShippingLocation

# Create your views here.
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializer



class UserRetrieveUpdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer


class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class =  BookingSerializer





class InsertBookingWithAddress(generics.ListCreateAPIView):

    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.all()


    def perform_create(self, serializer):
        user_data =  self.request.data.get('user_data', {})
        location_data = self.request.data.get('location_data', [])

        # Serialize and save the Author instance
        author_serializer = BookingSerializer(data=user_data)
        author_serializer.is_valid(raise_exception=True)
        author_serializer.save()
        # author = serializer.save(**user_data)

        # Get the ID of the newly created author
        author_id = author_serializer.data['user_id']

        # Create and save each Book instance associated with the author
        locations = []
        for location_info in location_data:
            location_data_index = {
                "full_name": location_info['full_name'],
                "country": location_info['country'],
                "phone_number": location_info['phone_number'],
                "address": location_info['address'],
                "state": location_info['state'],
                "zip_code": location_info['zip_code'],
                "ingestion_center": location_info['ingestion_center'],
                'user_id': author_id
            }
            location_serializer = ShippingLocationSerializer(data=location_data_index)
            location_serializer.is_valid(raise_exception=True)
            location =  location_serializer.save()
            locations.append(location)

        print(locations)
        locations_serializer = ShippingLocationSerializer(locations, many=True)
        # Include the serialized book_data in the response
        serializer.locations = locations_serializer.data
        print(serializer)

    def post(self, request, *args, **kwargs):
        # Ensure we use the serializer_class to handle the Author data
        serializer = self.get_serializer(data=request.data.get('user_data', {}))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    



class shippingViewSet(viewsets.ModelViewSet):
    queryset = ShippingLocation.objects.all()
    serializer_class = ShippingLocationSerializer



class BookingRetrieveUpdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Booking.objects.all()
    serializer_class = BookingSerializer