class BaseMnjError(BaseException):
    pass


class ClientError(BaseMnjError):
    pass


class BaseRegistryError(BaseMnjError):
    pass


class ClassAlreadyRegisteredError(BaseRegistryError):
    pass


class ClassIsNotRegisteredError(BaseRegistryError):
    pass
