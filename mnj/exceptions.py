class BaseMnjError(BaseException):
    pass


class BaseDocRegistryError(BaseMnjError):
    pass


class ClassAlreadyRegisteredError(BaseDocRegistryError):
    pass


class ClassIsNotRegisteredError(BaseDocRegistryError):
    pass
