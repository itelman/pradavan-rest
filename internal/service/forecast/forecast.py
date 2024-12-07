from sqlalchemy.orm import Session

from internal.repository.sqlite.forecasts import ForecastRepository
from pkg.open_weather.api import ForecastData


class ForecastService:
    def __init__(self, db: Session):
        self.forecast_repository = ForecastRepository(db)

    def Create(self, data: ForecastData) -> int:
        city, temp, pressure, humidity, description = data.city.capitalize(), data.temp, data.pressure, data.humidity, data.description
        return self.forecast_repository.Create(city, temp, pressure, humidity, description)

    def Get(self, id: int):
        return self.forecast_repository.ReadByID(id)

    def Delete(self, id: int):
        self.forecast_repository.Delete(id)

    def Update(self, id: int, data: ForecastData):
        temp, pressure, humidity, description = data.temp, data.pressure, data.humidity, data.description

        self.forecast_repository.Update(id, temp, pressure, humidity, description)

    def GetAll(self):
        return self.forecast_repository.ReadAll()
