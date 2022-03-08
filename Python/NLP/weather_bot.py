#!/usr/bin/env python
# coding: utf-8


import requests
import json
from datetime import datetime, timedelta


# get your location by your public IP address
_res = requests.get('https://ipinfo.io/')
_data = _res.json()
# get my current location via request
CITY = _data['city']
LOCATION = _data['loc'].split(',')
LATTITUDE = LOCATION[0]
LONGITUDE = LOCATION[1]


def kelvinToCelsius(kelvin):
    return kelvin - 273.15


def current_weather():
    # Current Weather Data
    city_name = CITY
    api_key = "your api key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    current_json = response.json()
    if current_json["cod"] != "404":
        # store the value of "main" key in variable y
        main_value = current_json["main"]

        current_temperature = main_value["temp"]
        current_pressure = main_value["pressure"]
        current_humidity = main_value["humidity"]

        weather = current_json["weather"]
        weather_description = weather[0]["description"]

        # print following values
        # print(f" Temperature (Celsius): {kelvinToCelsius(current_temperature):.2f}" +
        #       f"\n Atmospheric pressure (in hPa unit): {current_pressure}" +
        #       f"\n Humidity (in percentage): {current_humidity}" +
        #       f"\n Description: {weather_description}")
    else:
        print("===City not found or invalid API key.===")
    
    return current_json


def detail_weather_forecast():
    # Detailed forecast for the next 4 days
    api_key = "your api key"
    lat = LATTITUDE
    lon = LONGITUDE
    part = None
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
    response = requests.get(url)
    detail_weather_json = response.json()
    try: 
        current = detail_weather_json['current']
        minutely = detail_weather_json['minutely']
        hourly = detail_weather_json['hourly']
        daily = detail_weather_json['daily']

        local_time = datetime.utcfromtimestamp(current['dt']) + timedelta(hours=-5)
        local_time_str = local_time.strftime('%Y-%m-%d %H:%M:%S')
        current_temp = current['temp']
        current_feel = current['feels_like']
        current_uv = current['uvi']
        current_description = current['weather'][0]['description']

        next_minute = minutely[0]
        next_hour = hourly[0]

        next_description = next_hour['weather'][0]['description']
        next_precip = next_minute['precipitation']
        # print following values
        # print(f" Current local time: {local_time_str}" +
        #     f"\n Temperature (Celsius): {kelvinToCelsius(current_temp):.2f}" +
        #     f"\n Currently feels like (Celsius): {kelvinToCelsius(current_feel):.2f}" +
        #     f"\n Current UV index: {current_uv}" +
        #     f"\n Description: {current_description}"+
        #     f"\n Next hour weather: {next_description}"+
        #     f"\n Next hour precipitation: {next_precip}%")
    except:
        print("===City not found or invalid API key.===")
        
    return detail_weather_json


