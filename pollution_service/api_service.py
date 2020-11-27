import requests


BASE_URL = 'https://api.waqi.info/feed'
TOKEN = 'b50601bf3f57d6ab4c3ca5ce19bd39e4f7ca6bad'


class PollutionService:
    def __init__(self):
        pass

    def get_city(self, city):
        url = f'{BASE_URL}/{city}/?token={TOKEN}'
        data = requests.get(url).json()['data']
        return data

    def get_ip_city(self, ip):
        url = f'http://ip-api.com/json/{ip}'
        data = requests.get(url).json()
        return data['city']
