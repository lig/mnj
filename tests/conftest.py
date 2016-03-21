import pytest


@pytest.fixture(scope='session')
def mongo_client():
    from pymongo import MongoClient
    from mnj import d
    client = MongoClient(document_class=d)
    return client


@pytest.fixture(scope='session')
def database(mongo_client):
    mongo_client.drop_database('test')
    return mongo_client.test


@pytest.yield_fixture
def data(database):
    data = database.data
    data.drop()
    data.insert({'_id': '11', 'a': 1, 'b': 1})
    data.insert({'_id': '22', 'a': 2, 'b': 2})
    data.insert({'_id': '33', 'a': 3, 'b': 3})
    data.insert({'_id': '14', 'a': 1, 'b': 4})
    data.insert({'_id': '25', 'a': 2, 'b': 5})
    data.insert({'_id': '36', 'a': 3, 'b': 6})
    yield data


@pytest.yield_fixture
def doc_registry():
    from mnj.document.registry import Registry, registry
    Registry._registry = {}
    yield registry
    Registry._registry = {}
