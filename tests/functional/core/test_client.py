import pymongo
import pytest

import nj
import nj.core.client
import nj.core.exceptions


def test_001_create_default_client(mongo_host):
    nj.create_client(db_name='test', host=mongo_host)
    assert isinstance(nj.core.client.get_client(), pymongo.MongoClient)
    del nj.core.client._client_registry[nj.core.client._DEFAULT_CLIENT_NAME]


def test_002_create_named_client(mongo_host):
    nj.create_client(db_name='test', name='other_client', host=mongo_host)
    assert isinstance(
        nj.core.client.get_client(name='other_client'), pymongo.MongoClient
    )
    del nj.core.client._client_registry['other_client']


def test_003_recreating_client_is_forbidden(mongo_host):
    nj.create_client(db_name='test', host=mongo_host)
    with pytest.raises(nj.core.exceptions.ClientError):
        nj.create_client(db_name='test', host=mongo_host)
    del nj.core.client._client_registry[nj.core.client._DEFAULT_CLIENT_NAME]


def test_004_mongo_client_gets_any_kwargs(mongo_host):
    nj.create_client(db_name='test', host=mongo_host, tz_aware=True)
    assert nj.core.client.get_client().codec_options.tz_aware is True
    del nj.core.client._client_registry[nj.core.client._DEFAULT_CLIENT_NAME]


def test_005_default_document_class_is_mnj_factory(mongo_host):
    nj.create_client(db_name='test', host=mongo_host)
    assert (
        nj.core.client.get_client().codec_options.document_class is nj.DocumentFactory
    )
    del nj.core.client._client_registry[nj.core.client._DEFAULT_CLIENT_NAME]


def test_006_document_class_could_be_overrided(mongo_host):
    nj.create_client(db_name='test', host=mongo_host, document_class=dict)
    assert nj.core.client.get_client().codec_options.document_class is dict
    del nj.core.client._client_registry[nj.core.client._DEFAULT_CLIENT_NAME]
