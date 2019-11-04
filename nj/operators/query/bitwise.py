import typing

import bson.binary

from nj import operators


__all__ = ['bits_all_set_', 'bits_any_set_', 'bits_all_clear_', 'bits_any_clear_']

bitmask_T = typing.TypeVar(
    'bitmask_T', bson.binary.Binary, int, bytes, typing.Iterable[int]
)


class BitwiseOperator(operators.UnaryOperator):
    def __init__(self, bitmask: bitmask_T) -> None:
        super().__init__(bitmask)

    def prepare(  # type: ignore
        self, value: bitmask_T
    ) -> typing.Union[bson.binary.Binary, int, typing.Iterable[int]]:  # type: ignore

        if isinstance(value, (bson.binary.Binary, int)):
            return value

        if isinstance(value, bytes):
            return bson.binary.Binary(value)

        if isinstance(value, typing.Iterable) and all(
            isinstance(item, int) for item in value
        ):
            return value

        raise operators.MnjOperatorError(
            "`bitmask` must be one of: `bson.Binary`, `int`, `bytes` or iterable of"
            " integers"
        )


class bits_all_set_(BitwiseOperator):
    pass


class bits_any_set_(BitwiseOperator):
    pass


class bits_all_clear_(BitwiseOperator):
    pass


class bits_any_clear_(BitwiseOperator):
    pass
