from http import HTTPStatus


class UnauthorizedError(Exception):
    def __init__(self, msg: str = HTTPStatus.UNAUTHORIZED.phrase):
        super().__init__(msg)


class NotFoundError(Exception):
    def __init__(self):
        super().__init__(HTTPStatus.NOT_FOUND.phrase)


class ForbiddenError(Exception):
    def __init__(self, msg: str = HTTPStatus.FORBIDDEN.phrase):
        super().__init__(msg)
