from django.shortcuts import render
from .forms import SearchForm
from .models import WeatherData

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            # Assuming you have a field 'location' in your WeatherData model
            weather_data = WeatherData.objects.filter(location=location).first()
            # You may want to handle cases where weather_data is None if location doesn't exist
            context = {
                'form': form,
                'weather_data': weather_data,
            }
            return render(request, 'weather/search_results.html', context)
    else:
        form = SearchForm()
    return render(request, 'weather/search.html', {'form': form})
