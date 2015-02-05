import pytest

from mnj.query import *


def test_query_empty():
    query = q()
    assert query == {}
    query = q({})
    assert query == {}


def test_query_dict():
    query = q({'a': 1, 'b': 2})
    assert query == {'a': 1, 'b': 2}
    query = q({'a': 1, 'b': {'$gt': 1}})
    assert query == {'a': 1, 'b': {'$gt': 1}}


def test_query_kwargs():
    query = q(a=1, b=2)
    assert query == {'a': 1, 'b': 2}
    query = q(a=1, b={'$gt': 1})
    assert query == {'a': 1, 'b': {'$gt': 1}}


def test_query_illegal_value():
    with pytest.raises(TypeError):
        q([1, 2])
    with pytest.raises(ValueError):
        q('abc')
    with pytest.raises(TypeError):
        q(0)
    with pytest.raises(TypeError):
        q(1)


def test_query_from_query():
    query = q(q())
    assert query == {}
    query = q(q({'a': 1, 'b': 2}))
    assert query == {'a': 1, 'b': 2}


def test_query_and_query():
    query = q({'a': 1, 'b': 2}) & q({'a': 1, 'c': 3})
    assert query == {'a': 1, 'b': 2, 'c': 3}


def test_query_or_query():
    query = q({'a': 1, 'b': 2}) | q({'a': 1, 'c': 3})
    assert query == {'$or': [{'a': 1, 'b': 2}, {'a': 1, 'c': 3}]}
