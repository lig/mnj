from ..query import q

__all__ = ['_or']


def _or(first, second):
    return q({'$or': [q(first), q(second)]})
