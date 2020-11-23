from django.shortcuts import render
from .api_service import PollutionService


def index(request):
    service = PollutionService()
    data = service.get_city('seoul')
    data = data['iaqi']
    context = {
        'data': data,
    }
    return render(request, 'index.html', context)