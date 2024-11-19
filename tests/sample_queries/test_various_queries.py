import mnj


def test_various_001(data):
    cur = data.find(mnj.q(a=mnj.in_(1, 2)))
    assert {doc["_id"] for doc in cur} == {"11", "22", "14", "25"}


def test_various_002(data):
    cur = data.find(mnj.q(b=mnj.mod_(3, 1)))
    assert {doc["_id"] for doc in cur} == {"11", "14"}


def test_various_003(data):
    cur = data.find(mnj.q(b=mnj.not_(mnj.gt_(2))) & mnj.q(b=mnj.ne_(1)))
    assert {doc["_id"] for doc in cur} == {"22"}
