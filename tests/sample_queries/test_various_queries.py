import nj


def test_various_001(data):
    cur = data.find(nj.q(a=nj.in_(1, 2)))
    assert {doc['_id'] for doc in cur} == {'11', '22', '14', '25'}


def test_various_002(data):
    cur = data.find(nj.q(b=nj.mod_(3, 1)))
    assert {doc['_id'] for doc in cur} == {'11', '14'}


def test_various_003(data):
    cur = data.find(nj.q(b=nj.not_(nj.gt_(2))) & nj.q(b=nj.ne_(1)))
    assert {doc['_id'] for doc in cur} == {'22'}
