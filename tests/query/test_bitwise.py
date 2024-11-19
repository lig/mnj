import bson.binary
import pytest

import mnj


@pytest.mark.parametrize(
    "func,op",
    [
        (mnj.bits_all_set_, "$bitsAllSet"),
        (mnj.bits_any_set_, "$bitsAnySet"),
        (mnj.bits_all_clear_, "$bitsAllClear"),
        (mnj.bits_any_clear_, "$bitsAnyClear"),
    ],
)
def test_bitwise(func, op):
    query = func(bson.binary.Binary(b"*"))
    assert query == {op: bson.binary.Binary(b"*")}

    query = func(b"*")
    assert query == {op: bson.binary.Binary(b"*")}

    query = func(42)
    assert query == {op: 42}

    query = func([1, 3, 5])
    assert query == {op: [1, 3, 5]}
