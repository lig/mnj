class BaseMnjException(BaseException):
    pass


class BaseDocRegistryException(BaseMnjException):
    pass


class ClassAlreadyRegisteredError(BaseDocRegistryException):
    pass


class ClassIsNotRegistered(BaseDocRegistryException):
    pass
