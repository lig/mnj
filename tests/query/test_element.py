import mnj


def test_exists():
    query = mnj.q({"a": mnj.exists_(1)})
    assert query == {"a": {"$exists": True}}


def test_type():
    query = mnj.q({"a": mnj.type_(2)})
    assert query == {"a": {"$type": 2}}

    query = mnj.q({"a": mnj.type_("String")})
    assert query == {"a": {"$type": 2}}

    query = mnj.q({"a": mnj.type_(mnj.BSON_STRING)})
    assert query == {"a": {"$type": 2}}
