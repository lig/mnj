import pytest

from mnj.base import MongoClient, Database, Collection, Cursor


@pytest.yield_fixture
def mongo_client():
    client = MongoClient()
    yield client
    client.close()


@pytest.yield_fixture
def database(mongo_client):
    mongo_client.drop_database('test')
    yield mongo_client.test


@pytest.yield_fixture
def data(database):
    data = database.data
    data.drop()
    data.insert({'a': 1, 'b': 2})
    data.insert({'a': 3, 'b': 4})
    data.insert({'a': 5, 'b': 6})
    yield data


def test_mongo_client_uses_mnj_database(mongo_client):
    db = mongo_client.test
    assert isinstance(db, Database)


def test_database_uses_mnj_collection(database):
    col = database.data
    assert isinstance(col, Collection)


def test_collection_uses_mnj_cursor(data):
    cur = data.find()
    assert isinstance(cur, Cursor)
