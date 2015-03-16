import pytest

from mnj.operators.logical import _and, _or
from mnj.query import q


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
    q1 = q({'a': 1, 'b': 2})
    q2 = q({'a': 1, 'c': 3})
    assert q1 & q2 == _and(q1, q2)


def test_query_or_query():
    q1 = q({'a': 1, 'b': 2})
    q2 = q({'a': 1, 'c': 3})
    assert q1 | q2 == _or(q1, q2)
