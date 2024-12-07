from datetime import datetime

from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import DateTime

from internal.repository.models.base import Base


class Forecast(Base):
    __tablename__ = 'forecasts'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    city = Column(String, unique=True, nullable=False)
    temp = Column(Numeric, nullable=False)
    pressure = Column(Integer, nullable=False)
    humidity = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
