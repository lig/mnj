from mnj.operators.base import Operator, Arity
from mnj.query import q


__all__ = ['and_', 'nor_', 'not_', 'or_']


class _binary(Operator):
    arity = Arity.many

    def prepare(self, value):
        return [q(query) for query in value]


class and_(_binary):
    pass


class nor_(_binary):
    pass


class not_(Operator):

    def prepare(self, value):
        return q(value)


class or_(_binary):
    pass
