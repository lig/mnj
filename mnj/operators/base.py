import enum

import six

from mnj.document.query import Query

from .exceptions import MnjOperatorDefinitionError, MnjOperatorError


@enum.unique
class Arity(enum.Enum):
    many = 0
    one = 1


class OperatorMeta(type):

    def __new__(cls, name, bases, attrs):
        attrs['name'] = name
        attrs['Sname'] = '$' + name.rstrip('_')

        type_new = type.__new__(cls, name, bases, attrs)

        if not isinstance(type_new.arity, Arity):
            raise MnjOperatorDefinitionError(
                '`Operator.arity` attr must be instance of the `Arity` enum.')

        return type_new


@six.add_metaclass(OperatorMeta)
class Operator(Query):
    """Base class for MongoDB operators definitions.
    :param Arity arity: The arity of the operator. Defaults to `Arity.one`.
    """
    arity = Arity.one

    def __init__(self, *value):
        if self.arity == Arity.one:
            if len(value) != 1:
                raise MnjOperatorError(
                    '`{}` operator takes exactly one argument.')
            value = value[0]
        Query.__init__(self, [(self.Sname, self.prepare(value))])

    def prepare(self, value):
        return value
