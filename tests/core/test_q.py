import pytest

import nj


def test_query_empty():
    query = nj.q()
    assert query == {}
    query = nj.q({})
    assert query == {}


def test_query_dict():
    query = nj.q({'a': 1, 'b': 2})
    assert query == {'a': 1, 'b': 2}
    query = nj.q({'a': 1, 'b': {'$gt': 1}})
    assert query == {'a': 1, 'b': {'$gt': 1}}


def test_query_kwargs():
    query = nj.q(a=1, b=2)
    assert query == {'a': 1, 'b': 2}
    query = nj.q(a=1, b={'$gt': 1})
    assert query == {'a': 1, 'b': {'$gt': 1}}


def test_query_illegal_value():
    with pytest.raises(TypeError):
        nj.q([1, 2])
    with pytest.raises(ValueError):
        nj.q('abc')
    with pytest.raises(TypeError):
        nj.q(0)
    with pytest.raises(TypeError):
        nj.q(1)


def test_query_from_query():
    query = nj.q(nj.q())
    assert query == {}
    query = nj.q(nj.q({'a': 1, 'b': 2}))
    assert query == {'a': 1, 'b': 2}


def test_query_and_query():
    q1 = nj.q({'a': 1, 'b': 2})
    q2 = nj.q({'a': 1, 'c': 3})
    assert q1 & q2 == nj.and_(q1, q2)


def test_query_or_query():
    q1 = nj.q({'a': 1, 'b': 2})
    q2 = nj.q({'a': 1, 'c': 3})
    assert q1 | q2 == nj.or_(q1, q2)


def test_query_from_query_arguments():
    query = nj.q(nj.q({'a': 1}), nj.q({'b': 2}))
    assert query == {'a': 1, 'b': 2}
