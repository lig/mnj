import typing

from nj import core


class OperatorMeta(type):
    def __new__(
        cls,
        name: str,
        bases: typing.Tuple[typing.Type],
        attrs: typing.Dict[str, typing.Any],
    ) -> 'OperatorMeta':
        name_chunks = name.rstrip('_').split('_')
        attrs['Sname'] = (
            '$'
            + name_chunks[0]
            + ''.join(chunk.capitalize() for chunk in name_chunks[1:])
        )
        return typing.cast(OperatorMeta, super().__new__(cls, name, bases, attrs))


class Operator(core.Q, metaclass=OperatorMeta):
    """Base class for MongoDB variadic operator definition."""

    Sname: typing.ClassVar[str]

    def __init__(self, *values: typing.Any) -> None:
        super().__init__([(self.Sname, self.prepare(*values))])

    def prepare(self, *values: typing.Any) -> typing.Any:
        return values


class UnaryOperator(Operator):
    """Base class for MongoDB unary operator definition."""

    def __init__(self, value: typing.Any) -> None:
        super().__init__(value)

    def prepare(self, value: typing.Any) -> typing.Any:  # type: ignore
        return value


class ArgsOperator(Operator):
    def prepare(self, *values: typing.Any) -> typing.List[core.MongoObject]:
        return [core.MongoObject(query) for query in values]
