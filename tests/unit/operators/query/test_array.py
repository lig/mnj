import pytest

from nj import *
from nj.operators.exceptions import MnjOperatorError


def test_all():
    query = all_('bar', 42, None)
    assert query == {'$all': ('bar', 42, None,)}


def test_elem_match():
    query = elem_match_(q(gte_(80), lt_(85)))
    assert query == {'$elemMatch': {'$gte': 80, '$lt': 85}}

    query = elem_match_({'$gte': 80, '$lt': 85})
    assert query == {'$elemMatch': {'$gte': 80, '$lt': 85}}


def test_size():
    query = size_(2)
    assert query == {'$size': 2}

    with pytest.raises(MnjOperatorError):
        size_('two')

    with pytest.raises(MnjOperatorError):
        size_('2')

    with pytest.raises(MnjOperatorError):
        size_(2.0)
