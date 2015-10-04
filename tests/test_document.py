from mnj import *


def test_mongo_client_uses_mnj_doc(data):
    cur = data.find()
    assert all(isinstance(doc, d) for doc in cur)
