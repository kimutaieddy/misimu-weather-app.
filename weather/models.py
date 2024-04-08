# Create your models here.
# In weather/models.py

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    # Add more fields as needed

    def __str__(self):
        return f"Weather data for {self.location.name}"

