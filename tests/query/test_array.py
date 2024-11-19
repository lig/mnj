import pytest

import mnj
import mmnj.operators


def test_all():
    query = mnj.all_("bar", 42, None)
    assert query == {"$all": ("bar", 42, None)}


def test_elem_match():
    query = mnj.elem_match_(mnj.q(mnj.gte_(80), mnj.lt_(85)))
    assert query == {"$elemMatch": {"$gte": 80, "$lt": 85}}

    query = mnj.elem_match_({"$gte": 80, "$lt": 85})
    assert query == {"$elemMatch": {"$gte": 80, "$lt": 85}}


def test_size():
    query = mnj.size_(2)
    assert query == {"$size": 2}

    with pytest.raises(mnj.operators.MnjOperatorError):
        mnj.size_("two")

    with pytest.raises(mnj.operators.MnjOperatorError):
        mnj.size_("2")

    with pytest.raises(mnj.operators.MnjOperatorError):
        mnj.size_(2.0)
