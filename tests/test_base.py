import pytest
from mnj.base import Doc
from pymongo import MongoClient


@pytest.yield_fixture
def mongo_client():
    client = MongoClient(document_class=Doc)
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


def test_mongo_client_uses_mnj_doc(data):
    cur = data.find()
    assert all(isinstance(doc, Doc) for doc in cur)
