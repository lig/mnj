from collections import OrderedDict

__all__ = ['q']


class Query(OrderedDict):

    def __and__(self, other):
        new = self.copy()
        new.update(q(other))
        return new

    def __or__(self, other):
        from .operators import _or
        return _or(self, other)

q = Query
