import typing

import attr
import pymongo

from . import exceptions, registry


_DEFAULT_CLIENT_NAME = 'default'


@attr.s(auto_attribs=True, kw_only=True)
class _ClientEntry:
    client: pymongo.MongoClient
    db_name: str


_client_registry: typing.MutableMapping[str, _ClientEntry] = {}


def create_client(
    db_name: str,
    name: str = _DEFAULT_CLIENT_NAME,
    document_class: type = registry.DocumentFactory,
    **kwargs: typing.Any,
) -> None:
    if name in _client_registry:
        raise exceptions.ClientError(f"Client named `{name}` is already created")

    _client_registry[name] = _ClientEntry(
        client=pymongo.MongoClient(document_class=document_class, **kwargs),
        db_name=db_name,
    )


def get_client(name: str = _DEFAULT_CLIENT_NAME) -> pymongo.MongoClient:
    if name not in _client_registry:
        raise exceptions.ClientError(f"No client named `{name}` found")

    return _client_registry[name].client


def get_entry(client_name: str = _DEFAULT_CLIENT_NAME) -> _ClientEntry:
    if client_name not in _client_registry:
        raise exceptions.ClientError(f"No client named `{client_name}` found")

    return _client_registry[client_name]


def get_db(client_name: str = _DEFAULT_CLIENT_NAME) -> pymongo.database.Database:
    client_entry = get_entry(client_name)
    return client_entry.client[client_entry.db_name]
