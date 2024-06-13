from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Vehicle(models.Model):
    VEHICLE_TYPES = (
            ('SUV', 'SUV'),
            ('Sedan', 'Sedan'),
            ('Hatchback', 'Hatchback'),
            ('Truck', 'Truck'),
            ('Bus', 'Bus'),
    )
    name = models.CharField(max_length=150)
    vehicle_type = models.CharField(max_length=30, choices=VEHICLE_TYPES)
    description = models.TextField()
    daily_rates = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)



    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} - {self.vehicle}'
