import typing

import bson.regex

from nj import compat, core, operators


__all__ = ['mod_', 'regex_', 'text_', 'where_']

regex_T = typing.TypeVar('regex_T', bson.regex.Regex, compat.Pattern, str)


class mod_(operators.Operator):
    def __init__(self, divisor: int, remainder: int) -> None:
        super().__init__(divisor, remainder)


class regex_(operators.Operator):
    def __init__(self, regex: regex_T, options: typing.Optional[int] = None) -> None:
        """`regex` could be any type of:
         * `bson.regex.Regex`
         * compiled Python regex
         * JS regex pattern
        """
        super().__init__(regex, options)

    def prepare(  # type: ignore
        self, regex: regex_T, options: typing.Optional[int]
    ) -> bson.regex.Regex:  # type: ignore

        if isinstance(regex, compat.Pattern):
            regex = bson.regex.Regex.from_native(regex)
        elif isinstance(regex, str):
            regex = bson.regex.Regex(regex)

        if not isinstance(regex, bson.regex.Regex):
            raise operators.MnjOperatorError(
                "`regex` must be an instance of compiled `re` pattern, `str` or `bson.regex.Regex`"
            )

        regex.flags |= options if options is not None else 0
        return regex


class text_(operators.Operator):
    def __init__(
        self,
        search: str,
        language: typing.Optional[str] = None,
        caseSensitive: typing.Optional[bool] = None,
        diacriticSensitive: typing.Optional[bool] = None,
    ) -> None:
        super().__init__(search, language, caseSensitive, diacriticSensitive)

    def prepare(  # type: ignore
        self,
        search: str,
        language: typing.Optional[str] = None,
        caseSensitive: typing.Optional[bool] = None,
        diacriticSensitive: typing.Optional[bool] = None,
    ) -> core.MongoObject:  # type: ignore
        value = core.MongoObject()
        value['$search'] = search
        if language is not None:
            value['$language'] = language
        if caseSensitive is not None:
            value['$caseSensitive'] = caseSensitive
        if diacriticSensitive is not None:
            value['$diacriticSensitive'] = diacriticSensitive
        return value


class where_(operators.UnaryOperator):
    pass
