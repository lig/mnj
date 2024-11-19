import mnj


def test_simple_001(data):
    cur = data.find(mnj.q(a=1))
    assert {doc["_id"] for doc in cur} == {"11", "14"}


def test_simple_002(data):
    cur = data.find(mnj.q(a=mnj.ne_(2)))
    assert {doc["_id"] for doc in cur} == {"11", "33", "14", "36"}


def test_simple_003(data):
    cur = data.find(mnj.q(b=mnj.gt_(3)))
    assert {doc["_id"] for doc in cur} == {"14", "25", "36"}


def test_simple_004(data):
    cur = data.find(mnj.q(a=3) | mnj.q(b=2))
    assert {doc["_id"] for doc in cur} == {"22", "33", "36"}


def test_simple_005(data):
    cur = data.find(mnj.and_(mnj.q(a=1), mnj.q(b=4)))
    assert {doc["_id"] for doc in cur} == {"14"}
