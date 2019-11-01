import pytest

from nj import *
from nj.document.document import Doc


def test_mongo_client_uses_mnj_doc(data):
    cur = data.find()
    assert all(isinstance(doc, d) for doc in cur)


def test_doc_keeps_order():
    doc1 = d([('a', 1), ('b', 2)])
    doc2 = d([('b', 3), ('a', 4)])

    assert list(doc1.items()) == [('a', 1), ('b', 2)]
    assert list(doc2.items()) == [('b', 3), ('a', 4)]


def test_magic_auto_defined_name(doc_registry):
    class D(Doc):
        meta = {'magic': True}

    assert D._cls == 'D'


def test_magic_meta_defined_name(doc_registry):
    class D(Doc):
        meta = {'magic': True, 'class_name': 'Foo'}

    assert D._cls == 'Foo'


@pytest.mark.xfail
def test_doc_inheritance(data, doc_registry):
    class D(Doc):
        meta = {'magic': True}

    d = D(foo='bar')

    assert isinstance(d, D)

    data.insert_one(d)
    d_id = d['_id']
    del d
    d = data.find_one(q(_id=d_id))

    assert isinstance(d, D)
