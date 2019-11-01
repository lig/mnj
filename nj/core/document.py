import abc
import collections.abc
import typing

import attr
import bson
import pymongo

from . import base, client, query, registry


@attr.s(auto_attribs=True, kw_only=True)
class DocumentMeta:
    client_name: str = client._DEFAULT_CLIENT_NAME
    collection_name: str
    query_class: typing.Type[query.Query]


class DocumentType(abc.ABCMeta):
    def __new__(
        cls,
        name: str,
        bases: typing.Tuple[type, ...],
        namespace: typing.Dict[str, typing.Any],
    ) -> 'DocumentMeta':
        return attr.s(auto_attribs=True, kw_only=True)(
            super().__new__(cls, name, bases, namespace)
        )

    def __call__(cls, **kwargs: typing.Any) -> 'Document':
        if '_id' in kwargs:
            kwargs['id'] = kwargs.pop('_id')
        return super().__call__(**kwargs)

    @property
    def _col(cls) -> pymongo.collection.Collection:
        return client.get_db(client_name=cls._meta.client_name)[
            cls._meta.collection_name
        ]


class Document(collections.abc.MutableMapping, metaclass=DocumentType):
    _meta: typing.ClassVar[DocumentMeta]
    _col: typing.ClassVar[pymongo.collection.Collection]
    _id: bson.ObjectId = attr.ib(factory=bson.ObjectId)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        _metadata = {
            'collection_name': cls.__name__[:1].lower() + cls.__name__[1:],
            'query_class': query.Query,
        }

        if hasattr(cls, '_meta'):
            _metadata.update(attr.asdict(cls._meta))

        if hasattr(cls, 'Meta'):
            _metadata.update(
                (k, v) for k, v in vars(cls.Meta).items() if not k.startswith('_')
            )
            del cls.Meta

        cls._meta = DocumentMeta(**_metadata)
        registry.class_registry.register_class(cls)

    def __str__(self):
        return str(base.MongoObject(attr.asdict(self)))

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __delitem__(self, key):
        return NotImplemented

    def __iter__(self):
        return (attrs_attr.name for attrs_attr in self.__attrs_attrs__)

    def __len__(self):
        return len(self.__attrs_attrs__)

    @classmethod
    def query(cls, *args, **kwargs) -> query.Query:
        return cls._meta.query_class(*args, document_class=cls, **kwargs)
