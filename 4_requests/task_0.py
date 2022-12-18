from dataclasses import dataclass
import requests

@dataclass
class Weather:
    longitude: float
    latitude: float
    temperature: float
    feels_like: float
    pressure: int
    humidity: int
    clouds: int


def get_weather_for_point(longitude: float, latitude: float) -> Weather:
    """
    Napisz funkcję która pobierze pogodę dla punktu o podanej szerokości i długości geograficznej
    używając endpointu: https://openweathermap.org/api/one-call-api.

    Tips:
    0. Dokumentacja: https://openweathermap.org/api/one-call-api
    1. Aby otrzymać klucz trzeba się najpierw zarejestrować
    2. Dane muszą być w systemie METRYCZNYM!
    3. W dokumentacji są przykłady oraz opis wyszystkich query paramów

    Przykład:
    >>> get_weather_for_point(20, 30)
    Weather(longitude=20, latitude=30, temperature=18.03, feels_like=17.09, pressure=1020, humidity=46, clouds=10)
    """
    api_key = 'c6d72bf7d57f7b82ca8923912c901681'
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric')
    json_weaher = r.json()
    longitude = longitude
    latitude = latitude
    temperature = json_weaher["main"]["temp"]
    feels_like = json_weaher["main"]["feels_like"]
    pressure = json_weaher["main"]["pressure"]
    humidity = json_weaher["main"]["humidity"]
    clouds = json_weaher["clouds"]["all"]

    return Weather(longitude, latitude, temperature, feels_like, pressure, humidity, clouds)
