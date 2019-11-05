import nj


def test_gt():
    query = nj.q(a=nj.gt_(1))
    assert query == {'a': {'$gt': 1}}


def test_gte():
    query = nj.q(a=nj.gte_(1))
    assert query == {'a': {'$gte': 1}}


def test_in():
    query = nj.q(a=nj.in_(1, 2, 3))
    assert query == {'a': {'$in': (1, 2, 3)}}


def test_lt():
    query = nj.q(a=nj.lt_(1))
    assert query == {'a': {'$lt': 1}}


def test_lte():
    query = nj.q(a=nj.lte_(1))
    assert query == {'a': {'$lte': 1}}


def test_ne():
    query = nj.q(a=nj.ne_(1))
    assert query == {'a': {'$ne': 1}}


def test_nin():
    query = nj.q(a=nj.nin_(1, 2, 3))
    assert query == {'a': {'$nin': (1, 2, 3)}}
