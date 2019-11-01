from nj import *


def test_and():
    query = q(and_({'a': 1}, {'b': 2}))
    assert query == {'$and': [{'a': 1}, {'b': 2}]}


def test_nor():
    query = q(nor_({'a': 1}, {'b': 2}))
    assert query == {'$nor': [{'a': 1}, {'b': 2}]}


def test_not():
    query = q(not_({'a': 1}))
    assert query == {'$not': {'a': 1}}


def test_or():
    query = q(or_({'a': 1}, {'b': 2}))
    assert query == {'$or': [{'a': 1}, {'b': 2}]}
