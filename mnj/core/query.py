import typing

from . import base


if typing.TYPE_CHECKING:
    from . import document  # noqa: F401


class Q(base.MongoObject):
    def __and__(self, other: typing.Union["Q", typing.Mapping]) -> "Q":
        from nj import and_

        return and_(self, other)

    def __or__(self, other: typing.Union["Q", typing.Mapping]) -> "Q":
        from nj import or_

        return or_(self, other)


class Query(Q):
    _document_class: typing.Type["document.Document"]

    def __init__(
        self,
        *args: typing.Any,
        document_class: typing.Type["document.Document"],
        **kwargs: typing.Any,
    ) -> None:
        self._document_class = document_class
        super().__init__(*args, **kwargs)

    def __getattribute__(self, name: str) -> typing.Any:
        if not name.startswith("_") and hasattr(self._document_class._col, name):
            return getattr(self._document_class._col, name)
        return super().__getattribute__(name)
