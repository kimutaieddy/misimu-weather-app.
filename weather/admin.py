
# Register your models here.
# In weather/admin.py

from django.contrib import admin
from .models import Location, WeatherData

# Register your models here.
admin.site.register(Location)
admin.site.register(WeatherData)
