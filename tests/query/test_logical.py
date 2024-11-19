import mnj


def test_and():
    query = mnj.q(mnj.and_({"a": 1}, {"b": 2}))
    assert query == {"$and": [{"a": 1}, {"b": 2}]}


def test_nor():
    query = mnj.q(mnj.nor_({"a": 1}, {"b": 2}))
    assert query == {"$nor": [{"a": 1}, {"b": 2}]}


def test_not():
    query = mnj.q(mnj.not_({"a": 1}))
    assert query == {"$not": {"a": 1}}


def test_or():
    query = mnj.q(mnj.or_({"a": 1}, {"b": 2}))
    assert query == {"$or": [{"a": 1}, {"b": 2}]}
