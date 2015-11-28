from six import string_types

from mnj.query import q
from mnj.types import BSONType


__all__ = ['exists_', 'type_']


def exists_(value):
    return q({'$exists': bool(value)})


def type_(value):
    if isinstance(value, BSONType):
        value = value.value
    elif isinstance(value, string_types):
        value = BSONType[value].value
    return q({'$type': int(value)})
