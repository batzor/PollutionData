from django.shortcuts import render
from .api_service import PollutionService


POLLUTANTS = [('pm25', 'PM2.5'), ('pm10', 'PM10'), ('no2', 'NO2'), ('so2', 'SO2'), ('co', 'CO')]


def format_pollution_data(data):
    return [(value, str(data[key]['v']) + ' µg/m³') for key, value in POLLUTANTS]


def home(request):
    context = None
    error_message = None
    if request.method == 'POST':
        try:
            city = request.POST.get('city_name')
            service = PollutionService()
            data = service.get_city(city)
            data = data['iaqi']
            context = {
                'data': format_pollution_data(data),
                'current_name': city
            }
        except:
            context = {
                'error_message': 'No city found'
            }
    return render(request, 'home.html', context)


def recommendation(request):
    context = None
    return render(request, 'base.html', context)