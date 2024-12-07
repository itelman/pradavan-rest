import os
from typing import Any

import requests
from fastapi import HTTPException

url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")


class ForecastData:
    city: str
    json_data: Any
    temp: float
    pressure: int
    humidity: int
    description: str

    def __init__(self, city: str):
        self.city = city

        params = {"q": city, "appid": API_KEY}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            self.json_data = response.json()
        else:
            raise HTTPException(status_code=response.status_code)

        main = self.json_data.get("main")
        self.temp = main.get("temp")
        self.pressure = main.get("pressure")
        self.humidity = main.get("humidity")
        self.description = self.json_data.get("weather")[0].get("description")
