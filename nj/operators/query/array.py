import typing

from nj import core, operators


__all__ = ['all_', 'elem_match_', 'size_']


class all_(operators.Operator):
    def __init__(self, *values: typing.Any) -> None:
        super().__init__(*values)


class elem_match_(operators.UnaryOperator):
    def __init__(self, query: core.MongoObject_T) -> None:
        super().__init__(query)

    def prepare(self, value: core.MongoObject_T) -> core.MongoObject:  # type: ignore
        return super().prepare(core.MongoObject(value))


class size_(operators.UnaryOperator):
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def prepare(self, value: int) -> int:  # type: ignore

        if not isinstance(value, int):
            raise operators.MnjOperatorError("`size` must be integer")

        return super().prepare(value)
