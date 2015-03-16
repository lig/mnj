from mnj.operators.element import _exists, _type
from mnj.query import q
from mnj.types import BSON_STRING


def test_exists():
    query = q({'a': _exists(1)})
    assert query == {'a': {'$exists': True}}


def test_type():
    query = q({'a': _type(2)})
    assert query == {'a': {'$type': 2}}

    query = q({'a': _type('String')})
    assert query == {'a': {'$type': 2}}

    query = q({'a': _type(BSON_STRING)})
    assert query == {'a': {'$type': 2}}
