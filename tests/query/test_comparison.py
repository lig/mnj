import mnj


def test_gt():
    query = mnj.q(a=mnj.gt_(1))
    assert query == {"a": {"$gt": 1}}


def test_gte():
    query = mnj.q(a=mnj.gte_(1))
    assert query == {"a": {"$gte": 1}}


def test_in():
    query = mnj.q(a=mnj.in_(1, 2, 3))
    assert query == {"a": {"$in": (1, 2, 3)}}


def test_lt():
    query = mnj.q(a=mnj.lt_(1))
    assert query == {"a": {"$lt": 1}}


def test_lte():
    query = mnj.q(a=mnj.lte_(1))
    assert query == {"a": {"$lte": 1}}


def test_ne():
    query = mnj.q(a=mnj.ne_(1))
    assert query == {"a": {"$ne": 1}}


def test_nin():
    query = mnj.q(a=mnj.nin_(1, 2, 3))
    assert query == {"a": {"$nin": (1, 2, 3)}}
