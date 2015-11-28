from mnj.query import q


__all__ = ['and_', 'nor_', 'not_', 'or_']


def and_(*queries):
    return q({'$and': [q(query) for query in queries]})


def nor_(*queries):
    return q({'$nor': [q(query) for query in queries]})


def not_(query):
    """TODO: check for supported $not arguments
    """
    return q({'$not': q(query)})


def or_(*queries):
    return q({'$or': [q(query) for query in queries]})
