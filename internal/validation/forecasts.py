from pydantic import BaseModel


class ForecastRequest(BaseModel):
    temp: float
    pressure: int
    humidity: int
    description: str
