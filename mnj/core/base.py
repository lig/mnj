import typing

import bson.json_util


class MongoObject(dict):
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        if len(args) > 1:
            q = self.__class__()
            for arg in args:
                q.update(arg)
            args = [q]  # type: ignore

        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return bson.json_util.dumps(self)


MongoObject_T = typing.TypeVar(
    "MongoObject_T",
    MongoObject,
    typing.Mapping[str, typing.Any],
    typing.Iterable[typing.Tuple[str, typing.Any]],
)
