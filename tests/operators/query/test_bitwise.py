from bson.binary import Binary
import pytest

from mnj import *


@pytest.mark.parametrize('func,op', [
    (bits_all_set_, '$bitsAllSet'),
    (bits_any_set_, '$bitsAnySet'),
    (bits_all_clear_, '$bitsAllClear'),
    (bits_any_clear_, '$bitsAnyClear'),
])
def test_bitwise(func, op):
    query = func(Binary(b'*'))
    assert query == {op: Binary(b'*')}

    query = func(b'*')
    assert query == {op: Binary(b'*')}

    query = func(42)
    assert query == {op: 42}

    query = func([1, 3, 5])
    assert query == {op: [1, 3, 5]}
