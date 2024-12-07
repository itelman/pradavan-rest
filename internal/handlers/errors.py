import traceback
from http import HTTPStatus

from fastapi import Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from internal.repository.models.errors import UnauthorizedError, ForbiddenError
from internal.service.services import Services, new_services


def DefaultErrorHandler(err: HTTPStatus, details, request=None):
    content = {"message": err.phrase, "details": details, "request": request}
    return JSONResponse(status_code=err.value, content=content)


async def ValidationErrorHandler(req: Request, exc: RequestValidationError):
    err = HTTPStatus.UNPROCESSABLE_ENTITY
    body = await req.json()

    return DefaultErrorHandler(err, exc.errors(), body)


async def ConflictErrorHandler(req: Request, exc: IntegrityError):
    err = HTTPStatus.CONFLICT
    body = await req.json()

    return DefaultErrorHandler(err, str(exc.orig), body)


def UnauthorizedErrorHandler(req: Request, exc: UnauthorizedError):
    err = HTTPStatus.UNAUTHORIZED

    return DefaultErrorHandler(err, str(exc))


def ForbiddenErrorHandler(req: Request, exc: ForbiddenError):
    err = HTTPStatus.FORBIDDEN

    return DefaultErrorHandler(err, str(exc))


def InternalServerHandler(req: Request, exc: Exception, services: Services = Depends(new_services)):
    services.loggers.errorLog.error(f"Error: {exc}\nTraceback: {traceback.format_exc()}")
    err = HTTPStatus.INTERNAL_SERVER_ERROR
    content = {"message": err.phrase, "details": str(exc)}

    return JSONResponse(status_code=err.value, content=content)
