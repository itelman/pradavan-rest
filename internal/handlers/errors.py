import traceback
from http import HTTPStatus

from fastapi import Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from internal.repository.models.errors import UnauthorizedError, ForbiddenError, NotFoundError
from internal.service.services import Services, new_services


def DefaultErrorHandler(err: HTTPStatus, details, request=None):
    content = {"message": err.phrase, "details": details, "request": request}
    return JSONResponse(status_code=err.value, content=content)


async def ValidationErrorHandler(req: Request, exc: RequestValidationError):
    err = HTTPStatus.UNPROCESSABLE_ENTITY
    data = None
    body = await req.body()
    if body:
        data = await req.json()

    return DefaultErrorHandler(err, exc.errors(), data)


async def ConflictErrorHandler(req: Request, exc: IntegrityError):
    err = HTTPStatus.CONFLICT
    data = None
    body = await req.body()
    if body:
        data = await req.json()

    return DefaultErrorHandler(err, str(exc.orig), data)


def UnauthorizedErrorHandler(req: Request, exc: UnauthorizedError):
    err = HTTPStatus.UNAUTHORIZED

    return DefaultErrorHandler(err, str(exc))


def ForbiddenErrorHandler(req: Request, exc: ForbiddenError):
    err = HTTPStatus.FORBIDDEN

    return DefaultErrorHandler(err, str(exc))


def NotFoundHandler(req: Request, exc: NotFoundError):
    err = HTTPStatus.NOT_FOUND

    return DefaultErrorHandler(err, str(exc))


def InternalServerHandler(req: Request, exc: Exception, services: Services = Depends(new_services)):
    services.loggers.errorLog.error(f"Error: {exc}\nTraceback: {traceback.format_exc()}")
    err = HTTPStatus.INTERNAL_SERVER_ERROR
    content = {"message": err.phrase, "details": str(exc)}

    return JSONResponse(status_code=err.value, content=content)
