import nj


def test_and():
    query = nj.q(nj.and_({'a': 1}, {'b': 2}))
    assert query == {'$and': [{'a': 1}, {'b': 2}]}


def test_nor():
    query = nj.q(nj.nor_({'a': 1}, {'b': 2}))
    assert query == {'$nor': [{'a': 1}, {'b': 2}]}


def test_not():
    query = nj.q(nj.not_({'a': 1}))
    assert query == {'$not': {'a': 1}}


def test_or():
    query = nj.q(nj.or_({'a': 1}, {'b': 2}))
    assert query == {'$or': [{'a': 1}, {'b': 2}]}
