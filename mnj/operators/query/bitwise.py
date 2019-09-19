from collections import abc

import six
from bson.binary import Binary

from mnj.operators.base import UnaryOperator
from mnj.operators.exceptions import MnjOperatorError


__all__ = ['bits_all_set_', 'bits_any_set_', 'bits_all_clear_', 'bits_any_clear_']


class _bitwise(UnaryOperator):
    def __init__(self, bitmask):
        UnaryOperator.__init__(self, bitmask)

    def prepare(self, value):

        if isinstance(value, (Binary, int)):
            return value

        if isinstance(value, six.binary_type):
            return Binary(value)

        if isinstance(value, abc.Iterable) and all(
            isinstance(item, int) for item in value
        ):
            return value

        raise MnjOperatorError(
            '`bitmask` must be one of: `bson.Binary`, `int`, `{}` or'
            ' iterable of integers'.format(six.binary_type.__name__)
        )


class bits_all_set_(_bitwise):
    pass


class bits_any_set_(_bitwise):
    pass


class bits_all_clear_(_bitwise):
    pass


class bits_any_clear_(_bitwise):
    pass
