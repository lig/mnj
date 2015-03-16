from mnj.operators.logical import _and, _nor, _not, _or
from mnj.query import q


def test_and():
    query = q(_and({'a': 1}, {'b': 2}))
    assert query == {'$and': [{'a': 1}, {'b': 2}]}


def test_nor():
    query = q(_nor({'a': 1}, {'b': 2}))
    assert query == {'$nor': [{'a': 1}, {'b': 2}]}


def test_not():
    query = q(a=_not(1))
    assert query == {'a': {'$not': 1}}


def test_or():
    query = q(_or({'a': 1}, {'b': 2}))
    assert query == {'$or': [{'a': 1}, {'b': 2}]}
