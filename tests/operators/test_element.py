from mnj import *
from mnj.types import BSON_STRING


def test_exists():
    query = q({'a': exists_(1)})
    assert query == {'a': {'$exists': True}}


def test_type():
    query = q({'a': type_(2)})
    assert query == {'a': {'$type': 2}}

    query = q({'a': type_('String')})
    assert query == {'a': {'$type': 2}}

    query = q({'a': type_(BSON_STRING)})
    assert query == {'a': {'$type': 2}}
