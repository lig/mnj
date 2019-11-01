import os

import pytest


@pytest.fixture(scope='session')
def mongo_host():
    return os.getenv('MONGODB_HOST', 'localhost')


@pytest.fixture(scope='session')
def mongo_client(mongo_host):
    from pymongo import MongoClient

    client = MongoClient(host=mongo_host)
    return client


@pytest.fixture(scope='session')
def mnj_client(mongo_host):
    import nj

    nj.create_client(db_name='test', host=mongo_host)


@pytest.fixture(scope='session')
def db(mongo_client):
    mongo_client.drop_database('test')
    return mongo_client.test


@pytest.yield_fixture
def clean(mongo_client, db):
    yield
    mongo_client.drop_database(db.name)


@pytest.yield_fixture(autouse=True)
def doc_registry():
    from nj.core import registry

    registry.class_registry = registry.Registry()
    yield registry.class_registry
    registry.class_registry = registry.Registry()
