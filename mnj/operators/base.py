import six

from mnj.document.query import Query


class OperatorMeta(type):

    def __new__(cls, name, bases, attrs):
        attrs['Sname'] = '$' + name.rstrip('_')
        return type.__new__(cls, name, bases, attrs)


@six.add_metaclass(OperatorMeta)
class Operator(Query):
    """Base class for MongoDB variadic operator definition."""

    def __init__(self, *values):
        Query.__init__(self, [(self.Sname, self.prepare(*values))])

    def prepare(self, *values):
        return values


class UnaryOperator(Operator):
    """Base class for MongoDB unary operator definition."""

    def __init__(self, value):
        Operator.__init__(self, value)

    def prepare(self, value):
        return value
