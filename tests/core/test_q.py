import pytest

import mnj


def test_query_empty():
    query = mnj.q()
    assert query == {}
    query = mnj.q({})
    assert query == {}


def test_query_dict():
    query = mnj.q({"a": 1, "b": 2})
    assert query == {"a": 1, "b": 2}
    query = mnj.q({"a": 1, "b": {"$gt": 1}})
    assert query == {"a": 1, "b": {"$gt": 1}}


def test_query_kwargs():
    query = mnj.q(a=1, b=2)
    assert query == {"a": 1, "b": 2}
    query = mnj.q(a=1, b={"$gt": 1})
    assert query == {"a": 1, "b": {"$gt": 1}}


def test_query_illegal_value():
    with pytest.raises(TypeError):
        mnj.q([1, 2])
    with pytest.raises(ValueError):
        mnj.q("abc")
    with pytest.raises(TypeError):
        mnj.q(0)
    with pytest.raises(TypeError):
        mnj.q(1)


def test_query_from_query():
    query = mnj.q(mnj.q())
    assert query == {}
    query = mnj.q(mnj.q({"a": 1, "b": 2}))
    assert query == {"a": 1, "b": 2}


def test_query_and_query():
    q1 = mnj.q({"a": 1, "b": 2})
    q2 = mnj.q({"a": 1, "c": 3})
    assert q1 & q2 == mnj.and_(q1, q2)


def test_query_or_query():
    q1 = mnj.q({"a": 1, "b": 2})
    q2 = mnj.q({"a": 1, "c": 3})
    assert q1 | q2 == mnj.or_(q1, q2)


def test_query_from_query_arguments():
    query = mnj.q(mnj.q({"a": 1}), mnj.q({"b": 2}))
    assert query == {"a": 1, "b": 2}
