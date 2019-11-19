import nj


def test_simple_001(data):
    cur = data.find(nj.q(a=1))
    assert {doc['_id'] for doc in cur} == {'11', '14'}


def test_simple_002(data):
    cur = data.find(nj.q(a=nj.ne_(2)))
    assert {doc['_id'] for doc in cur} == {'11', '33', '14', '36'}


def test_simple_003(data):
    cur = data.find(nj.q(b=nj.gt_(3)))
    assert {doc['_id'] for doc in cur} == {'14', '25', '36'}


def test_simple_004(data):
    cur = data.find(nj.q(a=3) | nj.q(b=2))
    assert {doc['_id'] for doc in cur} == {'22', '33', '36'}


def test_simple_005(data):
    cur = data.find(nj.and_(nj.q(a=1), nj.q(b=4)))
    assert {doc['_id'] for doc in cur} == {'14'}
