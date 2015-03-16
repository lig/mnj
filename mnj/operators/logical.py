from ..query import q

__all__ = ['_and', '_nor', '_not', '_or']


def _and(*queries):
    return q({'$and': [q(query) for query in queries]})


def _nor(*queries):
    return q({'$nor': [q(query) for query in queries]})


def _not(query):
    """TODO: check for supported $not arguments
    """
    return q({'$not': q(query)})


def _or(*queries):
    return q({'$or': [q(query) for query in queries]})
