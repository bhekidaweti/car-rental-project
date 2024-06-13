from django.shortcuts import render
from rest_framework import viewsets
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer
# Create your views here.


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

            
