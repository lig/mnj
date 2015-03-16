from six import string_types

from ..query import q
from ..types import BSONType


__all__ = ['_exists', '_type']


def _exists(value):
    return q({'$exists': bool(value)})


def _type(value):
    if isinstance(value, BSONType):
        value = value.value
    elif isinstance(value, string_types):
        value = BSONType[value].value
    return q({'$type': int(value)})
