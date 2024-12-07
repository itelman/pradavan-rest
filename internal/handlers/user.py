from fastapi import APIRouter
from fastapi import Depends, Request
from starlette.responses import RedirectResponse

from internal.service.services import Services, new_services
from internal.validation.users import UserRequest
from pkg.auth.auth import CreateAccessToken
from pkg.open_weather.api import ForecastAPIData

router = APIRouter()


@router.post("/login")
def UserLogin(req: UserRequest, service: Services = Depends(new_services)):
    user = service.user_service.Authenticate(req)
    access_token = CreateAccessToken(data={"sub": str(user.id)})

    return {"message": "OK", "access_token": access_token, "token_type": "bearer"}


@router.post("/signup")
def UserSignup(req: UserRequest, service: Services = Depends(new_services)):
    service.user_service.Register(req)

    return {"message": "OK"}


@router.get("/ping")
def Ping(request: Request):
    return {"message": "OK", "test_response": ForecastAPIData("london"),
            "authenticated_user": getattr(request.state, 'user', None)}


@router.get("/")
def Ping():
    return RedirectResponse(url="/ping")
