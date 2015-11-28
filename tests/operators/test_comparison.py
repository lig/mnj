from mnj import *


def test_gt():
    query = q(a=gt_(1))
    assert query == {'a': {'$gt': 1}}


def test_gte():
    query = q(a=gte_(1))
    assert query == {'a': {'$gte': 1}}


def test_in():
    query = q(a=in_(1, 2, 3))
    assert query == {'a': {'$in': (1, 2, 3)}}


def test_lt():
    query = q(a=lt_(1))
    assert query == {'a': {'$lt': 1}}


def test_lte():
    query = q(a=lte_(1))
    assert query == {'a': {'$lte': 1}}


def test_ne():
    query = q(a=ne_(1))
    assert query == {'a': {'$ne': 1}}


def test_nin():
    query = q(a=nin_(1, 2, 3))
    assert query == {'a': {'$nin': (1, 2, 3)}}
