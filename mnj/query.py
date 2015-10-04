from .base import Doc


__all__ = ['q']


class Query(Doc):

    def __init__(self, *args, **kwargs):

        if len(args) > 1:
            query = q()
            for arg in args:
                query.update(arg)
            args = [query]

        Doc.__init__(self, *args, **kwargs)

    def __and__(self, other):
        from .operators import _and
        return _and(self, other)

    def __or__(self, other):
        from .operators import _or
        return _or(self, other)

q = Query
