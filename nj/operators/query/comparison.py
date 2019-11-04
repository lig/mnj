from nj import operators


__all__ = ['gt_', 'gte_', 'in_', 'lt_', 'lte_', 'ne_', 'nin_']


class gt_(operators.UnaryOperator):
    pass


class gte_(operators.UnaryOperator):
    pass


class in_(operators.Operator):
    pass


class lt_(operators.UnaryOperator):
    pass


class lte_(operators.UnaryOperator):
    pass


class ne_(operators.UnaryOperator):
    pass


class nin_(operators.Operator):
    pass
