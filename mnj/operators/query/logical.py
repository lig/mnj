from mnj.document.query import Query
from mnj.operators.base import Operator, UnaryOperator


__all__ = ['and_', 'nor_', 'not_', 'or_']


class _binary(Operator):

    def prepare(self, *values):
        return [Query(query) for query in values]


class and_(_binary):
    pass


class nor_(_binary):
    pass


class not_(UnaryOperator):

    def prepare(self, value):
        return Query(value)


class or_(_binary):
    pass
