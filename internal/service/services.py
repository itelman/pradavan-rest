from fastapi import Depends
from sqlalchemy.orm import Session

from internal.config.logger import Logger, loggers
from internal.service.forecast.forecast import ForecastService
from internal.service.user.user import UserService
from pkg.store.sql import NewSQL


class Services:
    user_service: UserService
    forecast_service: ForecastService

    def __init__(self, logger: Logger):
        self.loggers = logger

    def __call__(self, db: Session = Depends(NewSQL)):
        self.db_session = db
        self.user_service = UserService(db)
        self.forecast_service = ForecastService(db)

        return self


new_services = Services(loggers)
