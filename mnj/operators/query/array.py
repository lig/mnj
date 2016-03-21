from mnj.document.query import Query
from mnj.operators.base import Operator, UnaryOperator
from mnj.operators.exceptions import MnjOperatorError


__all__ = ['all_', 'elem_match_', 'size_']


class all_(Operator):

    def __init__(self, *values):
        Operator.__init__(self, *values)


class elem_match_(UnaryOperator):

    def __init__(self, query):
        UnaryOperator.__init__(self, query)

    def prepare(self, value):
        return UnaryOperator.prepare(self, Query(value))


class size_(UnaryOperator):

    def __init__(self, size):

        if not isinstance(size, int):
            raise MnjOperatorError('`size` must be integer')

        UnaryOperator.__init__(self, size)
