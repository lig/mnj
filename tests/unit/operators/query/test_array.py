import pytest

import nj
import nj.operators


def test_all():
    query = nj.all_('bar', 42, None)
    assert query == {'$all': ('bar', 42, None)}


def test_elem_match():
    query = nj.elem_match_(nj.q(nj.gte_(80), nj.lt_(85)))
    assert query == {'$elemMatch': {'$gte': 80, '$lt': 85}}

    query = nj.elem_match_({'$gte': 80, '$lt': 85})
    assert query == {'$elemMatch': {'$gte': 80, '$lt': 85}}


def test_size():
    query = nj.size_(2)
    assert query == {'$size': 2}

    with pytest.raises(nj.operators.MnjOperatorError):
        nj.size_('two')

    with pytest.raises(nj.operators.MnjOperatorError):
        nj.size_('2')

    with pytest.raises(nj.operators.MnjOperatorError):
        nj.size_(2.0)
