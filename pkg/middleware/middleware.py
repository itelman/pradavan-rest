import jwt
from fastapi import Request, FastAPI, Depends
from starlette.middleware.base import BaseHTTPMiddleware

from internal.repository.models.errors import ForbiddenError, UnauthorizedError
from internal.service.services import Services, new_services
from pkg.auth.auth import DecodeAccessToken


class BaseServiceMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, services: Services = Depends(new_services)):
        super().__init__(app)
        self.services = services


class LogRequestMiddleware(BaseServiceMiddleware):
    async def dispatch(self, request: Request, call_next):
        self.services.loggers.infoLog.info(f"{request.client.host} - {request.method} {request.url}")
        response = await call_next(request)
        return response


class Authenticate(BaseServiceMiddleware):
    async def dispatch(self, req: Request, call_next):
        auth_header = req.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

            try:
                payload = DecodeAccessToken(token)
                user_id = int(payload.get("sub"))

                user = self.services.user_service.Get(user_id)
                req.state.user = user
            except jwt.ExpiredSignatureError:
                raise UnauthorizedError("Session Expired")
            except Exception as e:
                raise e

        # Proceed to the next middleware or endpoint
        response = await call_next(req)
        return response


class VerifyAuthentication(BaseServiceMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        user = getattr(request.state, 'user', None)
        if user:
            if request.url.path.startswith("/login") or request.url.path.startswith("/signup"):
                raise ForbiddenError("User Authenticated")
        else:
            # Prevent unauthenticated users from accessing /user endpoints
            if request.url.path.startswith("/user"):
                raise UnauthorizedError("User Not Authenticated")

        return response
