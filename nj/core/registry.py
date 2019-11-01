import collections
import typing
import collections.abc
import bson

from . import client, exceptions


if typing.TYPE_CHECKING:
    from . import document  # noqa: F401


class Registry(object):
    def __init__(self) -> None:
        self._registry: typing.MutableMapping[
            str, typing.MutableMapping[str, typing.Type['document.Document']]
        ] = collections.defaultdict(dict)

    def register_class(self, document_class: typing.Type['document.Document']) -> None:

        client_name = document_class._meta.client_name
        collection_name = document_class._meta.collection_name

        if client_name in self._registry[collection_name]:
            raise exceptions.ClassAlreadyRegisteredError(
                f"Collection name `{collection_name}` cannot be registered for client"
                f" `{client_name}` and class `{document_class.__qualname__}` as it is"
                f" already in use"
            )

        self._registry[collection_name][client_name] = document_class

    def get_class(self, ns: str) -> typing.Type['document.Document']:

        database_name, _, collection_name = ns.partition('.')

        if collection_name not in self._registry:
            raise exceptions.ClassIsNotRegisteredError(
                f"Unknown collection name `{collection_name}`"
            )

        for client_name in self._registry[collection_name]:
            client_entry = client.get_entry(client_name=client_name)

            if client_entry.db_name == database_name:
                return self._registry[collection_name][client_name]

        raise exceptions.ClassIsNotRegisteredError(f"Class for ns `{ns}` not found")


class_registry = Registry()


class DocumentFactory(bson.raw_bson.RawBSONDocument, collections.abc.MutableMapping):
    def __new__(
        cls, bson_bytes: bytes, codec_options: typing.Optional[bson.CodecOptions] = None
    ) -> 'DocumentFactory':
        if codec_options is not None:
            codec_options = codec_options.with_options(document_class=dict)

        result = bson._bson_to_dict(bson_bytes, codec_options)

        if not {'cursor', 'ok'}.issubset(result):
            return result

        if 'ns' not in result['cursor']:
            return result

        batch_name = 'firstBatch' if 'firstBatch' in result['cursor'] else 'nextBatch'
        document_class = class_registry.get_class(result['cursor']['ns'])

        result['cursor'][batch_name] = [
            document_class(**doc) for doc in result['cursor'][batch_name]
        ]

        return result
