from mnj import *


def test_various_001(data):
    cur = data.find(q(a=in_(1, 2)))
    assert {doc['_id'] for doc in cur} == {'11', '22', '14', '25'}


def test_various_002(data):
    cur = data.find(q(b=mod_(3, 1)))
    assert {doc['_id'] for doc in cur} == {'11', '14'}


def test_various_003(data):
    cur = data.find(q(b=not_(gt_(2))) & q(b=ne_(1)))
    assert {doc['_id'] for doc in cur} == {'22'}
