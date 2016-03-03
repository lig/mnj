from mnj.operators.base import Operator, Arity
__all__ = ['gt_', 'gte_', 'in_', 'lt_', 'lte_', 'ne_', 'nin_']


class gt_(Operator):
    pass


class gte_(Operator):
    pass


class in_(Operator):
    arity = Arity.many


class lt_(Operator):
    pass


class lte_(Operator):
    pass


class ne_(Operator):
    pass


class nin_(Operator):
    arity = Arity.many
