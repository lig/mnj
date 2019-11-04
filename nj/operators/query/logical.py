from nj import core, operators


__all__ = ['and_', 'nor_', 'not_', 'or_']


class and_(operators.ArgsOperator):
    pass


class nor_(operators.ArgsOperator):
    pass


class not_(operators.UnaryOperator):
    def prepare(self, value: core.MongoObject_T) -> core.MongoObject:  # type: ignore
        return core.MongoObject(value)


class or_(operators.ArgsOperator):
    pass
