import collections
import collections.abc
import typing

import bson

from . import client, exceptions


if typing.TYPE_CHECKING:
    from . import document  # noqa: F401


class Registry(object):
    """ Document Classes Registry """

    # _registry: {collection_name: {client_name: {document_class_name: document_class}}}
    _registry: typing.MutableMapping[
        str,
        typing.MutableMapping[
            str, typing.MutableMapping[str, typing.Type['document.Document']]
        ],
    ]

    def __init__(self) -> None:
        self._registry = collections.defaultdict(lambda: collections.defaultdict(dict))

    def register_class(self, document_class: typing.Type['document.Document']) -> None:

        client_name = document_class._meta.client_name
        collection_name = document_class._meta.collection_name

        collection_registry = self._registry[collection_name][client_name]

        if collection_registry and not issubclass(
            document_class, next(iter(collection_registry.values()))
        ):
            raise exceptions.ClassAlreadyRegisteredError(
                f"Collection name `{collection_name}` cannot be registered for client"
                f" `{client_name}` and class `{document_class.__qualname__}` as it is"
                f" not a subclass of {next(iter(collection_registry.keys()))}"
            )

        collection_registry[document_class.__qualname__] = document_class

    def get_candidates(
        self, ns: str
    ) -> typing.MutableMapping[str, typing.Type['document.Document']]:

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
        document_class_candidates = class_registry.get_candidates(
            result['cursor']['ns']
        )
        document_class_default_name, document_class_default = next(
            iter(document_class_candidates.items())
        )

        result['cursor'][batch_name] = [
            document_class_candidates.get(
                doc.get('_nj_class', document_class_default_name),
                document_class_default,
            )(**doc)
            for doc in result['cursor'][batch_name]
        ]

        return result
