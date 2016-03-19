from six import string_types

from mnj.document.types import BSONType
from mnj.operators.base import UnaryOperator


__all__ = ['exists_', 'type_']


class exists_(UnaryOperator):

    def prepare(self, value):
        return bool(value)


class type_(UnaryOperator):

    def prepare(self, value):
        if isinstance(value, BSONType):
            value = value.value
        elif isinstance(value, string_types):
            value = BSONType[value].value
        return value
