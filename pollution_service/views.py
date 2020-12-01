from django.shortcuts import render
from .api_service import PollutionService


POLLUTANTS = [('pm25', 'PM2.5'), ('pm10', 'PM10'), ('no2', 'NO2'), ('so2', 'SO2'), ('co', 'CO')]


def format_pollution_data(data):
    return [(value, str(data[key]['v']) + ' µg/m³') for key, value in POLLUTANTS]


def home(request):
    context = None
    print(request.method)
    if request.method == 'GET':
        ip = None
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # for local testing, put placeholder
        if(ip == '127.0.0.1'):
            ip = '59.27.61.25'

        service = PollutionService()
        city = service.get_ip_city(ip)
        try:
            data = service.get_city(city)
            data = data['iaqi']
            context = {
                'data': format_pollution_data(data),
                'current_name': "Current Location: " + city
            }
        except:
            context = {
                'error_message': f'No information about {city} found'
            }
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
    ip = None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # for local testing, put placeholder
    if(ip == '127.0.0.1'):
        ip = '59.27.61.25'

    service = PollutionService()
    lon, lat = service.get_ip_lonlat(ip)
    context = {
        'lon': lon,
        'lat': lat
    }
    return render(request, 'recommendation.html', context)
