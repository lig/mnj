import nj


def test_exists():
    query = nj.q({'a': nj.exists_(1)})
    assert query == {'a': {'$exists': True}}


def test_type():
    query = nj.q({'a': nj.type_(2)})
    assert query == {'a': {'$type': 2}}

    query = nj.q({'a': nj.type_('String')})
    assert query == {'a': {'$type': 2}}

    query = nj.q({'a': nj.type_(nj.BSON_STRING)})
    assert query == {'a': {'$type': 2}}
