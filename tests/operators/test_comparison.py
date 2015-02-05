import pytest

from mnj.query import q
from mnj.operators import *


def test_gt():
    query = q(a=_gt(1))
    assert query == {'a': {'$gt': 1}}


def test_gte():
    query = q(a=_gte(1))
    assert query == {'a': {'$gte': 1}}


def test_in():
    query = q(a=_in(1, 2, 3))
    assert query == {'a': {'$in': (1, 2, 3)}}


def test_lt():
    query = q(a=_lt(1))
    assert query == {'a': {'$lt': 1}}


def test_lte():
    query = q(a=_lte(1))
    assert query == {'a': {'$lte': 1}}


def test_ne():
    query = q(a=_ne(1))
    assert query == {'a': {'$ne': 1}}


def test_nin():
    query = q(a=_nin(1, 2, 3))
    assert query == {'a': {'$nin': (1, 2, 3)}}
