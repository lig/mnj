import typing

from . import base


if typing.TYPE_CHECKING:
    from . import document


class Q(base.MongoObject):
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:

        if len(args) > 1:
            q = Q()
            for arg in args:
                q.update(arg)
            args = [q]  # type: ignore

        super().__init__(*args, **kwargs)

    def __and__(self, other: typing.Union['Q', typing.Mapping]) -> 'Q':
        from nj.operators import and_

        return and_(self, other)

    def __or__(self, other: typing.Union['Q', typing.Mapping]) -> 'Q':
        from nj.operators import or_

        return or_(self, other)


class Query(Q):
    _document_class: 'document.DocumentType'

    def __init__(self, *args, document_class: 'document.DocumentType', **kwargs):
        self._document_class = document_class
        super().__init__(*args, **kwargs)

    def __getattribute__(self, name: str) -> typing.Any:
        if not name.startswith('_') and hasattr(self._collection, name):
            return getattr(self._document_class._col, name)
        return super().__getattribute__(name)
