from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from internal.handlers.errors import UnauthorizedErrorHandler, ForbiddenErrorHandler, ConflictErrorHandler, \
    InternalServerHandler, ValidationErrorHandler
from internal.handlers.forecast import router as forecast_router
from internal.handlers.user import router as user_router
from internal.repository.models.errors import UnauthorizedError, ForbiddenError
from internal.service.services import new_services
from pkg.middleware.middleware import Authenticate, VerifyAuthentication, LogRequestMiddleware

app = FastAPI()

app.add_exception_handler(RequestValidationError, ValidationErrorHandler)
app.add_exception_handler(UnauthorizedError, UnauthorizedErrorHandler)
app.add_exception_handler(ForbiddenError, ForbiddenErrorHandler)
app.add_exception_handler(IntegrityError, ConflictErrorHandler)
app.add_exception_handler(Exception, InternalServerHandler)

app.add_middleware(LogRequestMiddleware, services=new_services)
app.add_middleware(Authenticate, services=new_services)
app.add_middleware(VerifyAuthentication, services=new_services)

app.include_router(user_router)
app.include_router(forecast_router)
