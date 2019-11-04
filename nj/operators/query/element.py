import typing

from nj import core, operators


__all__ = ['exists_', 'type_']


class exists_(operators.UnaryOperator):
    def prepare(self, value: typing.Union[bool, typing.Any]) -> bool:  # type: ignore
        return bool(value)


class type_(operators.UnaryOperator):
    def prepare(  # type: ignore
        self, value: typing.Union[core.BSONType, str]
    ) -> core.BSONType:  # type: ignore

        if isinstance(value, str):
            value = core.BSONType[value]

        if not isinstance(value, core.BSONType):
            raise operators.MnjOperatorError(
                "`type` must be an instance of `nj.BSONType` or `str`"
            )

        return value
