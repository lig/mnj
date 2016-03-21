import re

from bson.regex import Regex
import six

from mnj import *


def test_mod():
    query = q(mod_(2, 1))
    assert query == {'$mod': (2, 1)}

    query = q(mod_(divisor=2, remainder=1))
    assert query == {'$mod': (2, 1)}


def test_regex():
    pattern = r'(?:\d{3}|\(\d{3}\))([-\/\.])\d{3}\1\d{4}'
    query = q(regex_(Regex(pattern)))
    assert query == {'$regex': Regex(pattern)}

    query = q(regex_(Regex(pattern), re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE)}

    query = q(regex_(regex=Regex(pattern), options=re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE)}

    query = q(regex_(regex=re.compile(pattern), options=re.MULTILINE))
    assert query == {
        '$regex': Regex(pattern, re.MULTILINE | (six.PY3 and re.UNICODE))
    }

    query = q(regex_(regex=re.compile(pattern, re.MULTILINE)))
    assert query == {
        '$regex': Regex(pattern, re.MULTILINE | (six.PY3 and re.UNICODE))
    }

    query = q(regex_(regex=re.compile(pattern, re.MULTILINE)))
    assert query == {
        '$regex': Regex(pattern, re.MULTILINE | (six.PY3 and re.UNICODE))
    }

    query = q(regex_(pattern))
    assert query == {'$regex': Regex(pattern)}

    query = q(regex_(pattern, re.MULTILINE))
    assert query == {'$regex': Regex(pattern, re.MULTILINE)}


def test_text():
    query = q(text_('txt'))
    assert query == {'$text': {'$search': 'txt'}}

    query = q(text_('txt', 'da'))
    assert query == {'$text': {'$search': 'txt', '$language': 'da'}}

    query = q(text_('txt', 'da', False))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$caseSensitive': False,
        },
    }

    query = q(text_('txt', 'da', True))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$caseSensitive': True,
        },
    }

    query = q(text_('txt', 'da', diacriticSensitive=True))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$diacriticSensitive': True,
        },
    }

    query = q(text_('txt', 'da', False, False))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$caseSensitive': False,
            '$diacriticSensitive': False,
        },
    }

    query = q(text_('txt', 'da', False, True))
    assert query == {
        '$text': {
            '$search': 'txt',
            '$language': 'da',
            '$caseSensitive': False,
            '$diacriticSensitive': True,
        },
    }


def test_where():
    query = q(where_('javascript code'))
    assert query == {'$where': 'javascript code'}
