import nj


def test_mongo_client_uses_mongo_object(data, mnj_client):
    data = nj.get_db().data
    docs = list(data.find())
    assert all(isinstance(doc, nj.MongoObject) for doc in docs)


def test_mongo_object_keeps_order():
    doc1 = nj.MongoObject([('a', 1), ('b', 2)])
    doc2 = nj.MongoObject([('b', 3), ('a', 4)])

    assert list(doc1.items()) == [('a', 1), ('b', 2)]
    assert list(doc2.items()) == [('b', 3), ('a', 4)]
