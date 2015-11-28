from mnj.base import SortedDict


def test_sorted_dict():
    a = SortedDict({'c': 3, 'b': 2})
    assert list(a.keys()) == ['b', 'c']
    a['a'] = 1
    assert list(a.keys()) == ['a', 'b', 'c']
    a['d'] = 4
    assert list(a.keys()) == ['a', 'b', 'c', 'd']
    a['a'] = 5
    assert list(a.keys()) == ['a', 'b', 'c', 'd']
