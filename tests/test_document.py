from mnj import *
from mnj.document import Doc


def test_mongo_client_uses_mnj_doc(data):
    cur = data.find()
    assert all(isinstance(doc, d) for doc in cur)


def test_doc_keeps_order():
    doc1 = d([('a', 1), ('b', 2)])
    doc2 = d([('b', 3), ('a', 4)])

    assert list(doc1.items()) == [('a', 1), ('b', 2)]
    assert list(doc2.items()) == [('b', 3), ('a', 4)]


def test_doc_sort_parameter():

    class Document(Doc):
        meta = {
            'sorted': True
        }
    d = Document

    doc1 = d([('a', 1), ('b', 2)])
    doc2 = d([('b', 3), ('a', 4)])

    assert list(doc1.items()) == [('a', 1), ('b', 2)]
    assert list(doc2.items()) == [('a', 4), ('b', 3)]
