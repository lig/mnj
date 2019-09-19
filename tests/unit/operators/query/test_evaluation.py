import re

import six
from bson.regex import Regex

import mnj


def test_mod():
    query = mnj.q(mnj.mod_(2, 1))
    assert query == {'$mod': (2, 1)}

    query = mnj.q(mnj.mod_(divisor=2, remainder=1))
    assert query == {'$mod': (2, 1)}


def test_regex():
    pattern = r'(?:\d{3}|\(\d{3}\))([-\/\.])\d{3}\1\d{4}'
    query = mnj.q(mnj.regex_(Regex(pattern)))
    assert query == {'$regex': Regex(pattern)}

    query = mnj.q(mnj.regex_(Regex(pattern), re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE)}

    query = mnj.q(mnj.regex_(regex=Regex(pattern), options=re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE)}

    query = mnj.q(mnj.regex_(regex=re.compile(pattern), options=re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE | (six.PY3 and re.UNICODE))}

    query = mnj.q(mnj.regex_(regex=re.compile(pattern, re.MULTILINE)))
    assert query == {'$regex': Regex(pattern, re.MULTILINE | (six.PY3 and re.UNICODE))}

    query = mnj.q(mnj.regex_(regex=re.compile(pattern, re.MULTILINE)))
    assert query == {'$regex': Regex(pattern, re.MULTILINE | (six.PY3 and re.UNICODE))}

    query = mnj.q(mnj.regex_(pattern))
    assert query == {'$regex': Regex(pattern)}

    query = mnj.q(mnj.regex_(pattern, re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE)}


def test_text():
    query = mnj.q(mnj.text_('txt'))
    assert query == {'$text': {'$search': 'txt'}}

    query = mnj.q(mnj.text_('txt', 'da'))
    assert query == {'$text': {'$search': 'txt', '$language': 'da'}}

    query = mnj.q(mnj.text_('txt', 'da', False))
    assert query == {
        '$text': {'$search': 'txt', '$language': 'da', '$caseSensitive': False}
    }

    query = mnj.q(mnj.text_('txt', 'da', True))
    assert query == {
        '$text': {'$search': 'txt', '$language': 'da', '$caseSensitive': True}
    }

    query = mnj.q(mnj.text_('txt', 'da', diacriticSensitive=True))
    assert query == {
        '$text': {'$search': 'txt', '$language': 'da', '$diacriticSensitive': True}
    }

    query = mnj.q(mnj.text_('txt', 'da', False, False))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$caseSensitive': False,
            '$diacriticSensitive': False,
        }
    }

    query = mnj.q(mnj.text_('txt', 'da', False, True))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$caseSensitive': False,
            '$diacriticSensitive': True,
        }
    }


def test_where():
    query = mnj.q(mnj.where_('javascript code'))
    assert query == {'$where': 'javascript code'}
