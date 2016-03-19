import re

from bson import regex as bson_regex
import six

from mnj.document.document import Doc
from mnj.operators.base import Operator, UnaryOperator


__all__ = ['mod_', 'regex_', 'text_', 'where_']


class mod_(Operator):

    def __init__(self, divisor, remainder):
        Operator.__init__(self, divisor, remainder)


class regex_(Operator):

    def __init__(self, regex, options=None):
        """`regex` could be any type of:
         * `bson.regex.Regex`
         * compiled Python regex
         * JS regex pattern
        """
        Operator.__init__(self, regex, options)

    def prepare(self, regex, options):

        if isinstance(regex, re._pattern_type):
            regex = bson_regex.Regex.from_native(regex)

        if isinstance(regex, six.string_types):
            regex = bson_regex.Regex(regex)

        if isinstance(regex, bson_regex.Regex):
            regex.flags |= options or 0
            return regex


class text_(Operator):

    def __init__(
        self, search, language=None, caseSensitive=None,
        diacriticSensitive=None
    ):
        Operator.__init__(
            self, search, language, caseSensitive, diacriticSensitive)

    def prepare(self, search, language, caseSensitive, diacriticSensitive):
        value = Doc()
        value['$search'] = search
        if language is not None:
            value['$language'] = language
        if caseSensitive is not None:
            value['$caseSensitive'] = caseSensitive
        if diacriticSensitive is not None:
            value['$diacriticSensitive'] = diacriticSensitive
        return value


class where_(UnaryOperator):
    pass
