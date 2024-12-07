from http import HTTPStatus


class UnauthorizedError(Exception):
    def __init__(self):
        super().__init__(HTTPStatus.UNAUTHORIZED.phrase)


class NotFoundError(Exception):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND.phrase)


class ForbiddenError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
