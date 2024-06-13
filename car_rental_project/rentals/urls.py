from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, BookingViewSet




router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
        path('', include(router.urls)),
        
        ]
