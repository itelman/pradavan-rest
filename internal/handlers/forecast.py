from fastapi import APIRouter
from fastapi import Depends

from internal.service.services import Services, new_services
from internal.validation.forecasts import ForecastRequest
from pkg.open_weather.api import ForecastData, ForecastAPIData

router = APIRouter()

forecasts_url = "/user/forecasts"


@router.get(forecasts_url + "/create")
def Create(city: str, service: Services = Depends(new_services)):
    forecast_data = ForecastAPIData(city)
    forecast_id = service.forecast_service.Create(forecast_data)

    return {"message": "OK", "forecast_id": forecast_id}


@router.get(forecasts_url + "/{id}")
def Get(id: int, service: Services = Depends(new_services)):
    forecast = service.forecast_service.Get(id)

    return forecast


@router.get(forecasts_url)
def GetAll(service: Services = Depends(new_services)):
    forecasts = service.forecast_service.GetAll()

    return forecasts


@router.put(forecasts_url + "/{id}")
def Update(id: int, req: ForecastRequest, service: Services = Depends(new_services)):
    db_data = service.forecast_service.Get(id)
    forecast_data = ForecastData(db_data.city, req.temp, req.pressure, req.humidity, req.description)
    service.forecast_service.Update(id, forecast_data)

    return {"message": "OK"}


@router.put(forecasts_url + "/api/{id}")
def UpdateAPI(id: int, service: Services = Depends(new_services)):
    db_data = service.forecast_service.Get(id)
    forecast_data = ForecastAPIData(db_data.city)
    service.forecast_service.Update(id, forecast_data)

    return {"message": "OK"}


@router.delete(forecasts_url + "/{id}")
def Delete(id: int, service: Services = Depends(new_services)):
    service.forecast_service.Delete(id)

    return {"message": "OK"}
