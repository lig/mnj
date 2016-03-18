from mnj.document.query import Query
from mnj.operators.base import Operator, Arity


__all__ = ['and_', 'nor_', 'not_', 'or_']


class _binary(Operator):
    arity = Arity.many

    def prepare(self, value):
        return [Query(query) for query in value]


class and_(_binary):
    pass


class nor_(_binary):
    pass


class not_(Operator):

    def prepare(self, value):
        return Query(value)


class or_(_binary):
    pass
