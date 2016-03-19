from mnj.exceptions import BaseMnjError


class BaseRegistryError(BaseMnjError):
    pass


class ClassAlreadyRegisteredError(BaseRegistryError):
    pass


class ClassIsNotRegisteredError(BaseRegistryError):
    pass
