# Create your views here.
# In weather/views.py

from django.shortcuts import render
from .models import Location, WeatherData

def index(request):
    # Example view to display weather information
    locations = Location.objects.all()
    context = {
        'locations': locations,
    }
    return render(request, 'weather/index.html', context)
