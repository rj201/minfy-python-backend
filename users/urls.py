
from django.urls import path
from .views import UserListCreate, UserRetrieveUpdatedelete,BookingListCreate, BookingRetrieveUpdatedelete, InsertBookingWithAddress, shippingViewSet

urlpatterns = [
    path('users', UserListCreate.as_view(),name="Create-user-List"),
    path('user/<int:pk>/', UserRetrieveUpdatedelete.as_view(), name = 'user-Details'),

    path('booking', BookingListCreate.as_view(),name="Create-booking-List"),
    path('booking/<int:pk>/', BookingRetrieveUpdatedelete.as_view(), name = 'booking-Details'),

    path('bookingAdd', InsertBookingWithAddress.as_view(),name="Create-booking-List"),
    path('shipping', shippingViewSet.as_view({'get': 'list'}),name="Create-booking-List")
]
