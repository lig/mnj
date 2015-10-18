class BaseMnjException(BaseException):
    pass


class DocRegistryException(BaseMnjException):
    pass


class DocAlreadyRegisteredError(DocRegistryException):
    pass
