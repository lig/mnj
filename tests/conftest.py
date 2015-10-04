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
    data.insert({'a': 1, 'b': 2})
    data.insert({'a': 3, 'b': 4})
    data.insert({'a': 5, 'b': 6})
    yield data
