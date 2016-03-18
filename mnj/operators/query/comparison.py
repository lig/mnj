from mnj.operators.base import Operator, UnaryOperator


__all__ = ['gt_', 'gte_', 'in_', 'lt_', 'lte_', 'ne_', 'nin_']


class gt_(UnaryOperator):
    pass


class gte_(UnaryOperator):
    pass


class in_(Operator):
    pass


class lt_(UnaryOperator):
    pass


class lte_(UnaryOperator):
    pass


class ne_(UnaryOperator):
    pass


class nin_(Operator):
    pass
