class AppException(Exception):
    pass


class UnsupportedType(AppException):
    pass


class GameException(Exception):
    pass


class UserAlreadyExists(AppException):
    pass

class InvalidUserEmail(AppException):
    pass
