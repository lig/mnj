from mnj.document.base import BaseDoc


__all__ = ['q']


class Query(BaseDoc):

    def __init__(self, *args, **kwargs):

        if len(args) > 1:
            query = q()
            for arg in args:
                query.update(arg)
            args = [query]

        BaseDoc.__init__(self, *args, **kwargs)

    def __and__(self, other):
        from mnj import and_
        return and_(self, other)

    def __or__(self, other):
        from mnj import or_
        return or_(self, other)

q = Query
