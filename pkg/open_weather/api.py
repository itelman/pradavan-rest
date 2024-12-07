import os
from typing import Any

import requests
from fastapi import HTTPException

url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")


def get_response(city: str):
    params = {"q": city, "appid": API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        raise HTTPException(status_code=response.status_code)


class ForecastData:
    city: str
    temp: float
    pressure: int
    humidity: int
    description: str

    def __init__(self, city, temp, pressure, humidity, description):
        self.city = city
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity
        self.description = description


class ForecastAPIData(ForecastData):
    json_data: Any

    def __init__(self, city: str):
        self.json_data = get_response(city)
        main = self.json_data.get("main")
        temp = main.get("temp")
        pressure = main.get("pressure")
        humidity = main.get("humidity")
        description = self.json_data.get("weather")[0].get("description")

        super().__init__(city, temp, pressure, humidity, description)
