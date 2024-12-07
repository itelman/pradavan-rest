from sqlalchemy.orm import Session

from internal.repository.models import Forecast
from internal.repository.models.errors import NotFoundError


class ForecastRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, city: str, temp, pressure, humidity, description) -> int:
        try:
            new_forecast = Forecast(
                city=city,
                temp=temp,
                pressure=pressure,
                humidity=humidity,
                description=description
            )

            self.db.add(new_forecast)
            self.db.commit()

            return new_forecast.id
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByCity(self, city: str) -> Forecast:
        try:
            forecast = self.db.query(Forecast).filter(Forecast.city == city).first()
            if forecast:
                return forecast
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByID(self, id: int) -> Forecast:
        try:
            forecast = self.db.query(Forecast).filter(Forecast.id == id).first()
            if forecast:
                return forecast
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def Delete(self, id: int):
        try:
            forecast = self.ReadByID(id)
            self.db.delete(forecast)  # Mark the user for deletion
            self.db.commit()  # Commit to apply the deletion
        except Exception as e:
            self.db.rollback()
            raise e

    def Update(self, id: int, temp, pressure, humidity, description):
        try:
            forecast = self.ReadByID(id)
            forecast.temp, forecast.pressure, forecast.humidity, forecast.description = temp, pressure, humidity, description
            self.db.commit()  # Commit the change to the database
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadAll(self):
        try:
            return self.db.query(Forecast).all()
        except Exception as e:
            self.db.rollback()
            raise e
